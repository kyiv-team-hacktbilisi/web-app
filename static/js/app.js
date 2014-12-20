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
    .controller('AuthController', function ($scope, $http, $cookies, $state) {
        $scope.signIn = function () {
            console.log('Sending sign in request');
            $http.post('/api/auth/', {
                email: $scope.email,
                password: $scope.password
            }).then(function (result) {
                $cookies.loggedIn = true;
                $cookies.email = $scope.email;
                if (result.data.result === 'success') {
                    console.log('Logged in');
                    $state.go('logged.settings');
                } else {
                    console.log('/api/auth no result === success');
                }
            }, function () {
                console.log('/api/auth err connection');
            })
        };

        $scope.signUp = function () {
            console.log('Sending sign up request');
            $http.post('/api/user/', {
                email: $scope.email,
                password: $scope.password
            }).then(function (result) {
                $cookies.loggedIn = true;
                $cookies.email = $scope.email;
                if (result.data.result === 'success') {
                    console.log('Registered');
                    $scope.signIn();
                } else {
                    console.log('/api/user no result success');
                }
            }, function () {
                console.log('/api/user err connection');
            })
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
    .controller('SettingsController', function ($scope) {

    })
    .controller('TimetableController', function ($scope) {

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
