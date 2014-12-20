angular.module('app', ['ui.router', 'ngMaterial'])
    .config(function ($stateProvider, $urlRouterProvider) {
        $urlRouterProvider.when('', 'login');
        $stateProvider
            .state('login', {
                url: '/login',
                templateUrl: 'views/login.html'//,
                //controller: 'PageCtrl'
            });
    });
