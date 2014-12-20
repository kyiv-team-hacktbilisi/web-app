angular.module('app', ['ui.router', 'ngMaterial', 'ngCookies'])
    .config(function ($stateProvider, $urlRouterProvider) {
        $urlRouterProvider.when('', 'login');
        $stateProvider
            .state('login', {
                url: '/login',
                templateUrl: 'views/login.html',
                controller: 'LoginController'
            });
    })
    .controller('LoginController', function ($scope, $http, $cookies) {
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
    });
