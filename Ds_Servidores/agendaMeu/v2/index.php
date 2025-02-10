<?php

$uri = $_SERVER['REQUEST_URI'];
$method = $_SERVER['REQUEST_METHOD'];

switch ($method | $uri) {
    /*
    * Path: GET /api/users
    * Task: show all the users
    */
    case ($method == 'GET' && $uri == '/api/users'):
        break;
    /*
    * Path: GET /api/users/{id}
    * Task: get one user
    */
    case ($method == 'GET' && preg_match('/\/api\/users\/[1-9]/', $uri)):
        break;
    /*
    * Path: POST /api/users
    * Task: store one user
    */
    case ($method == 'POST' && $uri == '/api/users'):
        break;
    /*
    * Path: PUT /api/users/{id}
    * Task: update one user
    */
    case ($method == 'PUT' && preg_match('/\/api\/users\/[1-9]/', $uri)):
        break;
    /*
    * Path: DELETE /api/users/{id}
    * Task: delete one user
    */
    case ($method == 'DELETE' && preg_match('/\/api\/users\/[1-9]/', $uri)):
        break;
    /*
    * Path: ?
    * Task: this path doesn't match any of the defined paths
    *      throw an error
    */
    default:
        break;
 }