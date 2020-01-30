var react           = 'https://api.github.com/repos/facebook/react'
var angular         = 'https://api.github.com/repos/angular/angular'
var vue             = 'https://api.github.com/repos/vuejs/vue'
var ember           = 'https://api.github.com/repos/emberjs/ember.js'

var fetchbtn 	    = document.querySelector("#fetch");

// React
var react_issues    = document.querySelector("#react-issues");
var react_stars    	= document.querySelector("#react-stars");
var react_forks     = document.querySelector('#react-forks');

// Angular
var angular_issues  = document.querySelector('#angular-issues');
var angular_stars   = document.querySelector("#angular-stars");
var angular_forks   = document.querySelector('#angular-forks');

// Vue
var vue_issues      = document.querySelector('#vue-issues');
var vue_stars       = document.querySelector("#vue-stars");
var vue_forks       = document.querySelector('#vue-forks');

// Ember
var ember_issues    = document.querySelector('#ember-issues');
var ember_stars     = document.querySelector("#ember-stars");
var ember_forks     = document.querySelector('#ember-forks');

fetchbtn.addEventListener("click", function() {

    fetch(react)
    .then(function(req){
        req.json().then(function(data){
            react_issues.innerText      = data['open_issues'];
            react_stars.innerText       = data['stargazers_count'];
            react_forks.innerText       = data['forks_count'];
        })
    })
    .catch(function(){
        console.log("React Error");
    })

    fetch(angular)
    .then(function(req){
        req.json().then(function(data){
            angular_issues.innerText    = data['open_issues']
            angular_stars.innerText     = data['stargazers_count'];
            angular_forks.innerText     = data['forks_count']
        })
    })
    .catch(function(){
        console.log("Angular Error");
    })

    fetch(vue)
    .then(function(req){
        req.json().then(function(data){
            vue_issues.innerText        = data['open_issues']
            vue_stars.innerText         = data['stargazers_count'];
            vue_forks.innerText         = data['forks_count']
        })
    })
    .catch(function(){
        console.log("Vue Error");
    })

    fetch(ember)
    .then(function(req){
        req.json().then(function(data){
            ember_issues.innerText      = data['open_issues']
            ember_stars.innerText       = data['stargazers_count'];
            ember_forks.innerText       = data['forks_count']
        })
    })
    .catch(function(){
        console.log("Ember Error");
    })

});


