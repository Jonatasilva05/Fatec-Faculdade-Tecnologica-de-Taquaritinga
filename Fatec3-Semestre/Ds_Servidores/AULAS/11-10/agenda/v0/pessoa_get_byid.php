<?php
//  rota para consulta todos os contatos
require 'database.php'; // importação do metodos do arquivo database.php
$data = json_decode(file_get_contents('php://input'), true);
if ( isset($data["id"])){
    $id = $data["id"];
    try {
        $stmt = $conn->prepare("SELECT * FROM pessoas WHERE id = :id ");
        $stmt->bindParam(':id', $id );
        $stmt->execute();
        $pessoas = $stmt->fetchAll(PDO::FETCH_ASSOC);
        header('Content-Type: application/json');
        echo json_encode($pessoas);
    } catch(PDOException $e) {
        echo json_encode(['error' => $e->getMessage()]);
    }
} else {
    echo json_encode(['error' => 'O id é obrigatório']);
}
