<?php
require 'database.php';
$data = json_decode(file_get_contents('php://input'), true);
if (isset($data[ "id"])) {
    $id = $data['id'];
    try {
        $stmt = $conn->prepare('DELETE FROM pessoas WHERE id = :id') ;
        $stmt->bindParam(':id', $id);
        $stmt->execute();        
        echo json_encode(["message" => " Sucesso na exclusão !" ]);
    } catch(PDOException $e) {
        echo json_encode(['error' => $e->getMessage()]);
    }
} else {
    echo json_encode(['error' => 'O codigo é obrigatório']);
}