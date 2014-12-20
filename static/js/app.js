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
    .service('settings', function () {
        var saved = {
            classDuration: 90
        };
        this.save = function (data) {
            saved = data;
        };
        this.get = function () {
            return saved;
        };
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
    .controller('SettingsController', function ($scope, $state, settings) {
        $scope.user = settings.get();

        $scope.saveSettings = function () {
            $state.go('logged.timetable');
        };
    })
    .controller('TimetableController', function ($scope, $mdDialog) {
        $scope.days = [
            'Monday',
            'Tuesday',
            'Wednesday',
            'Thursday',
            'Friday'
        ];
        var oneDay = [
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
                teacher_name: "Mukha I. P.",
                type: "lection",
                start_time: "10:30",
                end_time: "12:10",
                color: "#4e6cef"
            }
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
    .run(function($rootScope, $state, $stateParams, auth) {
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
    });
