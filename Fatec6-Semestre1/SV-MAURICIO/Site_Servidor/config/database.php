<?php

$host = "localhost";
$user = "root";
$pass = "";
$db   = "novapay";

$conn = new mysqli($host, $user, $pass, $db);

if($conn->connect_error){
    die("Erro na conexão");
}

$conn->set_charset("utf8");
?>