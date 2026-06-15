<?php
$servername = "localhost";
$username = "root";     // Usuário do banco de dados
$password = "";         // Senha do banco de dados
$dbname = "serenus";    // Nome do banco de dados

// Criar conexão
$conn = new mysqli($servername, $username, $password, $dbname);

// Verificar conexão
if ($conn->connect_error) {
    die("Conexão com o banco de dados falhou: " . $conn->connect_error);
}
?>