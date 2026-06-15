<?php

include("../config/database.php");
include("../includes/header.php");
include("../includes/footer.php");


$nome = $_POST['nome'];
$email = $_POST['email'];
$telefone = $_POST['telefone'];

$stmt = $conn->prepare("
INSERT INTO clientes(nome,email,telefone)
VALUES(?,?,?)
");

$stmt->bind_param("sss",$nome,$email,$telefone);

$stmt->execute();

header("Location: ../pages/clientes.php");
?>
