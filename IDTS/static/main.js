angular.module('app', ['ngCookies'])

.config([
      '$httpProvider', 
      '$interpolateProvider', 
      function($httpProvider, $interpolateProvider) {
          $interpolateProvider.startSymbol('{$');
          $interpolateProvider.endSymbol('$}');
          $httpProvider.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';
          $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
      }]).
      run([
      '$http', 
      '$cookies', 
      function($http, $cookies) {
          $http.defaults.headers.post['X-CSRFToken'] = $cookies.csrftoken;
    }])
    
.controller('AppController', ['$scope', '$http', function($scope, $http) {
  
  var postData = {
    type : "start",
    numOfExercises : "4"
    
  };
  $http.post("/IDTS/", postData).
  then(function(response) {
    if(response)
      console.log(response);
  }, function(response) {  
    
  });
}]);