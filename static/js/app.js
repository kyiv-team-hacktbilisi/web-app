angular.module('app', ['ui.router', 'ngMaterial', 'ngCookies'])
    .config(function ($stateProvider, $urlRouterProvider) {
        $urlRouterProvider.when('', 'settings');
        $stateProvider
            .state('auth', {
                url: '/login',
                templateUrl: 'views/login.html',
                controller: 'AuthController'
            })
            .state('logged', {
                templateUrl: '/views/main.html',
                controller: 'MainController'
            })
            .state('logged.settings', {
                url: '/settings',
                views: {
                    'mainView': {
                        templateUrl: 'views/settings.html',
                        controller: 'SettingsController'
                    },
                    'titleView': {
                        template: 'Settings'
                    }
                }
            })
            .state('logged.timetable', {
                url: '/timetable',
                views: {
                    'mainView': {
                        templateUrl: 'views/timetable.html',
                        controller: 'TimetableController'
                    },
                    'titleView': {
                        template: 'Timetable'
                    }
                }
            });
    })
    .service('auth', function ($cookies) {
        this.loggedIn = function () {
            return $cookies.loggedIn;
        }
    })
    .service('settings', function ($window) {
        var saved = $window.localStorage;
        this.save = function (data) {
            //saved = data;
        };
        this.get = function () {
            return saved;
        };
    })
    .factory('addToGCalendar', function ($http, $cookies, $q) {
        var token = $cookies.google_access_token;
        return function (groupName, cb) {
            $http.post('/api/kpi_schedule/', {group: groupName})
                .success(function (classes) {
                    
                    console.log(classes);
                    var calendarId;
                    $http.post('https://www.googleapis.com/calendar/v3/calendars/?access_token=' + token, {
                        summary: "University schedule",
                        description: "Automatically updated schedule for NTUU \"KPI\"",
                        location: "НТУУ КПІ, Київ, Україна"
                    }).success(function (calendar) {
                        calendarId = calendar.id;
                        var ps = [];
                        for (var i = 0; i < classes.length; i++) {
                            var lesson = classes[i];
                            var date = moment([2014, 8, 1, 8, 0]).day(lesson.day_number);
                            if (lesson.lesson_week === '2') {
                                date.add(7, 'day');
                            }
                            if (date.day() > 14) {
                                date.add(14, 'day');
                            }
                            var day = date.day();
                            
                            ps.push($http.post(
                                'https://www.googleapis.com/calendar/v3/calendars/' + 
                                    calendarId + '/events?access_token=' + token, {
                                    summary: lesson.lesson_name,
                                    description: lesson.lesson_name + ' (' + lesson.lesson_type + ')',
                                    start: {
                                        dateTime: '2014-09-0' + day + 'T' + lesson.time_start,
                                        timeZone: 'Europe/Kiev'
                                    },
                                    end: {
                                        dateTime: '2014-09-0' + day + 'T' + lesson.time_end,
                                        timeZone: 'Europe/Kiev'
                                    },
                                    location: "НТУУ КПІ (" + lesson.lesson_room + ")"
                            }));
                        }
                        $q.all(ps).then(function () {
                            cb(true);
                        }, function () {
                            cb(false);
                        });
                    }).error(function () {
                        cb(false);
                    })
                })
                .error(function () {
                    cb(false);
                });
        }
    })
    .controller('AuthController', function ($scope, $http, $cookies, $state) {
        $scope.signIn = function () {
            console.log('Sending sign in request');
           // $http.post('/api/auth/', $scope.user).then(function (result) {
                $cookies.loggedIn = true;
                $cookies.email = $scope.email;
                if (true || result.status === 200) {
                    console.log('Logged in');
                    $state.go('logged.settings');
                } else {
                    console.log('/api/auth no result === success');
                }
            //}, function () {
            //    console.log('/api/auth err connection');
            //})
        };

        $scope.signUp = function () {
            console.log('Sending sign up request');
            //$http.post('/api/user/', $scope.user).then(function (result) {
                $cookies.loggedIn = true;
                $cookies.email = $scope.email;
                if (true ||result.status === 200) {
                    console.log('Registered');
                    $scope.signIn();
                } else {
                    console.log('/api/user no result success');
                }
            //}, function () {
            //    console.log('/api/user err connection');
            //})
        }
    })
    .controller('MainController', function ($scope, $state, $cookies) {
        $scope.logOut = function () {
            delete $cookies.loggedIn;
            delete $cookies.email;
            delete $cookies.password;
            $state.go('auth');
        }
    })
    .controller('SettingsController', function ($scope, $state, settings, addToGCalendar) {
        $scope.user = settings.get();
        $scope.user.university = "NTUU KPI";

        $scope.saveSettings = function () {
            $state.go('logged.timetable');
        };
    })
    .controller('TimetableController', function ($scope) {
        $scope.days = [
            'Monday',
            'Tuesday',
            'Wednesday',
            'Thursday',
            'Friday'
        ];

        $scope.classes = [
            [
                {
                    name: "Mathematics",
                    audience: "103",
                    teacher_name: "Mukha I. P.",
                    type: "lection",
                    start_time: "8:30",
                    end_time: "10:15",
                    color: "#4e6cef"
                },
                {
                    name: "Physics",
                    audience: "103",
                    teacher_name: "Rokoviy I. P.",
                    type: "lection",
                    start_time: "10:25",
                    end_time: "12:20",
                    color: "#4e6cef"
                },
                {
                    name: "English",
                    audience: "103",
                    teacher_name: "Pasichniy I. P.",
                    type: "lection",
                    start_time: "12:20",
                    end_time: "14:15",
                    color: "#4e6cef"
                }
            ], //mon
            [
                {
                    name: "Software Engineering",
                    audience: "103",
                    teacher_name: "Buzovskiy Q. P.",
                    type: "lection",
                    start_time: "10:30",
                    end_time: "12:10",
                    color: "#4e6cef"
                }
            ], //tue
            [
                {
                    name: "Computer Engineering",
                    audience: "103",
                    teacher_name: "Ivanov I. P.",
                    type: "lection",
                    start_time: "8:30",
                    end_time: "10:15",
                    color: "#4e6cef"
                },
                {
                    name: "Theory of algorithms",
                    audience: "103",
                    teacher_name: "Molchanovskiy I. O.",
                    type: "lection",
                    start_time: "10:25",
                    end_time: "12:20",
                    color: "#4e6cef"
                },
                {
                    name: "Computer science",
                    audience: "103",
                    teacher_name: "Mukha I. P.",
                    type: "lection",
                    start_time: "12:20",
                    end_time: "14:15",
                    color: "#4e6cef"
                }
            ], // wed
            [
                {
                    name: "Algorithms and DS",
                    audience: "103",
                    teacher_name: "Boldak  A. O.",
                    type: "lection",
                    start_time: "8:30",
                    end_time: "10:15",
                    color: "#4e6cef"
                },
                {
                    name: "Electrical Engineering",
                    audience: "103",
                    teacher_name: "Korochkin O. V",
                    type: "lection",
                    start_time: "10:25",
                    end_time: "12:20",
                    color: "#4e6cef"
                }
            ], // thir
            [
                {
                    name: "Computer modelling",
                    audience: "103",
                    teacher_name: "Saverchenko V.G.",
                    type: "lection",
                    start_time: "8:30",
                    end_time: "10:15",
                    color: "#4e6cef"
                },
                {
                    name: "Computer systems",
                    audience: "103",
                    teacher_name: "Lutrkiy G. M.",
                    type: "lection",
                    start_time: "10:25",
                    end_time: "12:20",
                    color: "#4e6cef"
                },
                {
                    name: "OOP",
                    audience: "103",
                    teacher_name: "Nevdaschenko M. V.",
                    type: "lection",
                    start_time: "12:20",
                    end_time: "14:15",
                    color: "#4e6cef"
                }
            ]
        ];
    })
    .run(function($rootScope, $state, $stateParams, auth, $cookies, addToGCalendar, $window) {
        $rootScope.$on('$stateChangeStart', function (event, toState, toStateParams) {
            // track the state the user wants to go to; authorization service needs this
            $rootScope.toState = toState;
            $rootScope.toStateParams = toStateParams;
            // if the principal is resolved, do an authorization check immediately. otherwise,
            // it'll be done when the state it resolved.
            if (toState.name === 'auth') {
                return;
            }
            if (!auth.loggedIn()) {
                event.preventDefault();
                console.log('you\'re not logged in');
                $state.go('auth');
            } else {
                console.log('logged in');
            }
        });
        
        if ($cookies.google_access_token) {

            addToGCalendar($window.localStorage.group, function (result) {
                console.log('Result of adding to gcal: ' + result);
                delete $cookies.google_access_token;
            });
        }
    });
