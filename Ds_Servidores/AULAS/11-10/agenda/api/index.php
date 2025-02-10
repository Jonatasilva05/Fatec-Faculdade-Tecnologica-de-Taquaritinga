<?php
//  rota para consulta todos os contatos
require '../database/config.php'; // importação do metodos do arquivo database.php

$uri = $_SERVER['REQUEST_URI'];

// captura o verbo sendo utilizado
$method = $_SERVER['REQUEST_METHOD'];

$uriParts = explode('/', trim($uri, '/')); // Divide a URI em partes e remove as barras extras

// Verifica se o ID está presente na URL
// if (isset($uriParts[3]) && is_numeric($uriParts[3])) {
//     $id = $uriParts[3];
// }
// echo "$uri";
$id = 0 ;
if (isset($_GET['id'])) {
    $id = $_GET['id'];
}    

switch ($method) {
    case ($method == 'GET'):
        if (!isset($id) || $id == 0) {
            getAll($conn);
        } else {
            getById($conn, $id);
        }      
        break;
    case ($method == 'POST'):
        post($conn);
        break;
    case ($method == 'PUT'):
        put($conn);
        break;
    case ($method == 'DELETE'):
        delete($conn);
        break;
    default:
        echo json_encode(['error' => "Verbo informada inexistente .."]);
        break;
}

function getAll($conn)
{
    try {
        $stmt = $conn->query('SELECT * FROM pessoas ORDER BY nome');
        $pessoas = $stmt->fetchAll(PDO::FETCH_ASSOC);
        header('Content-Type: application/json');
        echo json_encode($pessoas);
    } catch (PDOException $e) {
        echo json_encode(['error' => $e->getMessage()]);
    }
}

function post($conn)
{
    $data = json_decode(file_get_contents('php://input'), true);
    if (isset($data["nome"])) {
        $nome = $data['nome'];
        $telefone = $data['telefone'];
        $observacao = $data['observacao'];
        try {
            $stmt = $conn->prepare('INSERT INTO pessoas (nome,telefone,observacao) VALUES (:nome, :telefone, :observacao)');
            $stmt->bindParam(':nome', $nome);
            $stmt->bindParam(':telefone', $telefone);
            $stmt->bindParam(':observacao', $observacao);
            $stmt->execute();
            $pessoaId = $conn->lastInsertId();
            echo json_encode(['id' => $pessoaId, 'nome' => $nome, 'telefone' => $telefone]);
        } catch (PDOException $e) {
            echo json_encode(['error' => $e->getMessage()]);
        }
    } else {
        echo json_encode(['error' => 'O nome é obrigatório']);
    }
}

function put($conn)
{
    $data = json_decode(file_get_contents('php://input'), true);
    if (isset($data["id"])) {
        $id = $data['id'];
        $nome = $data['nome'];
        $telefone = $data['telefone'];
        $observacao = $data['observacao'];
        try {
            $stmt = $conn->prepare('UPDATE pessoas SET nome= :nome , telefone= :telefone ,observacao = :observacao WHERE id = :id ');
            $stmt->bindParam(':id', $id);
            $stmt->bindParam(':nome', $nome);
            $stmt->bindParam(':telefone', $telefone);
            $stmt->bindParam(':observacao', $observacao);
            $stmt->execute();

            echo json_encode(['id' => $id, 'nome' => $nome, 'telefone' => $telefone]);
        } catch (PDOException $e) {
            echo json_encode(['error' => $e->getMessage()]);
        }
    } else {
        echo json_encode(['error' => 'O id é obrigatório']);
    }
}

function delete($conn)
{
    $data = json_decode(file_get_contents('php://input'), true);
    if (isset($data["id"])) {
        $id = $data['id'];
        try {
            $stmt = $conn->prepare('DELETE FROM pessoas WHERE id = :id');
            $stmt->bindParam(':id', $id);
            $stmt->execute();
            echo json_encode(["message" => " Sucesso na exclusão !"]);
        } catch (PDOException $e) {
            echo json_encode(['error' => $e->getMessage()]);
        }
    } else {
        echo json_encode(['error' => 'O codigo é obrigatório']);
    }
}

function getById($conn, $id)
{
    // $data = json_decode(file_get_contents('php://input'), true);
    if (isset($id)) {
        try {
            $stmt = $conn->prepare("SELECT * FROM pessoas WHERE id = :id ");
            $stmt->bindParam(':id', $id);
            $stmt->execute();
            $pessoas = $stmt->fetchAll(PDO::FETCH_ASSOC);
            header('Content-Type: application/json');
            echo json_encode($pessoas);
        } catch (PDOException $e) {
            echo json_encode(['error' => $e->getMessage()]);
        }
    } else {
        echo json_encode(['error' => 'O id é obrigatório']);
    }
}
