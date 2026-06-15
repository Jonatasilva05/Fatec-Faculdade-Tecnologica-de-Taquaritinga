<?php

include("../config/database.php");
include("../includes/header.php");
include("../includes/footer.php");

$id = $_GET['id'];

$stmt = $conn->prepare("
DELETE FROM clientes
WHERE id=?
");

$stmt->bind_param("i",$id);

$stmt->execute();

header("Location: ../pages/clientes.php");
?>

