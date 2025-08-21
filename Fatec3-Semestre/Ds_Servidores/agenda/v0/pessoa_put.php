<?php
require 'database.php';
$data = json_decode(file_get_contents('php://input'), true);
if (isset($data[ "id"])) {
    $id = $data['id'];
    $nome = $data['nome'];
    $telefone = $data['telefone'];
    $observacao = $data['observacao'];
    try {
        $stmt = $conn->prepare('UPDATE pessoas SET nome= :nome , telefone= :telefone ,observacao = :observacao WHERE id = :id ' ) ;
        $stmt->bindParam(':id', $id);
        $stmt->bindParam(':nome', $nome);
        $stmt->bindParam(':telefone', $telefone);
        $stmt->bindParam(':observacao', $observacao);
        $stmt->execute();
        
        echo json_encode(['id' => $id, 'nome' => $nome, 'telefone' => $telefone ]);

    } catch(PDOException $e) {
        echo json_encode(['error' => $e->getMessage()]);
    }
} else {
    echo json_encode(['error' => 'O id é obrigatório']);
}