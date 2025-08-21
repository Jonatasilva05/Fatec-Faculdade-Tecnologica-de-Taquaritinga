<?php
//  rota para consulta todos os contatos
require '../database/config.php'; // importação do metodos do arquivo database.php

$uri = $_SERVER['REQUEST_URI'];

// captura o verbo sendo utilizado
$method = $_SERVER['REQUEST_METHOD'];

$uriParts = explode('/', trim($uri, '/')); // Divide a URI em partes e remove as barras extras
$id = 0 ;
// route params - end point = http://localhost/dsi/agenda/pessoas/1
// para funcionamento correto, necessario configurar arquivo .htacess, indicando a pasta do index.php
// exemplo do $uriParts com a uri = "http://localhost/dsi/agenda/pessoas/1"
// 0 - /dsi
// 1 - /agenda
// 2 - /pessoas
// 3 - id
// Verifica se o ID está presente na URL
if (isset($uriParts[3]) && is_numeric($uriParts[3])) {
    $id = $uriParts[3];
}
//
// $nelem =  sizeof ($uriParts);
// echo $nelem;
// query params - end point = http://localhost/dsi/agenda/pessoas?id=1
//  Verifica se o ID está presente na URL
// if (isset($_GET['id'])) {
//     $id = $_GET['id'];
// }    

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
        put($conn, $id);
        break;
    case ($method == 'DELETE'):
        delete($conn, $id);
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

function put($conn, $id)
{
    $data = json_decode(file_get_contents('php://input'), true);

    if (isset($id)) {
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

function delete($conn, $id)
{
    $data = json_decode(file_get_contents('php://input'), true);
    if (isset($id)) {
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
