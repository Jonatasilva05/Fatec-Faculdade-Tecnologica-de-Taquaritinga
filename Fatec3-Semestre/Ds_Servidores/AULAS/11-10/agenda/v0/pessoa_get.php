<?php
//  rota para consulta todos os contatos
require 'database.php'; // importação do metodos do arquivo database.php
try {
    $stmt = $conn->query('SELECT * FROM pessoas ORDER BY nome');
    $pessoas = $stmt->fetchAll(PDO::FETCH_ASSOC);
    header('Content-Type: application/json');
    echo json_encode($pessoas);
} catch(PDOException $e) {
    echo json_encode(['error' => $e->getMessage()]);
}