<?php
// Rota para consulta de todos os contatos
require 'database.php'; // Importação dos métodos do arquivo database.php

// Verifica se o parâmetro "id" foi passado pela URL
if (isset($_GET['id'])) {
    $id = $_GET['id'];
    try {
        // Prepara e executa a query para buscar a pessoa pelo ID
        $stmt = $conn->prepare("SELECT * FROM pessoas WHERE id = :id");
        $stmt->bindParam(':id', $id);
        $stmt->execute();
        $pessoas = $stmt->fetchAll(PDO::FETCH_ASSOC);

        // Define o tipo de conteúdo como JSON e retorna o resultado
        header('Content-Type: application/json');
        echo json_encode($pessoas);
    } catch(PDOException $e) {
        // Retorna o erro em formato JSON
        echo json_encode(['error' => $e->getMessage()]);
    }
} else {
    // Retorna erro caso o ID não tenha sido enviado
    echo json_encode(['error' => 'O id é obrigatório']);
}


// Como funciona agora:
// O ID deve ser passado como um parâmetro de URL, por exemplo: http://localhost/pessoa_get.php?id=1.
// O script agora captura o valor do ID através de $_GET['id'], que corresponde ao valor enviado na URL.