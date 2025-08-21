<?php
//  rota para consulta todos os contatos
require '../database/config.php'; // importação do metodos do arquivo database.php

$uri = $_SERVER['REQUEST_URI'];

// captura o verbo sendo utilizado
$method = $_SERVER['REQUEST_METHOD'];

$uriParts = explode('/', trim($uri, '/')); // Divide a URI em partes e remove as barras extras
$id = 0 ;

// route params - end point = http://localhost/dsi/agenda/ceps/1
// para funcionamento correto, necessario configurar arquivo .htacess, 
// indicando a pasta do index.php
// exemplo do $uriParts com a uri = "http://localhost/dsi/agenda/ceps/1"
// 0 - /dsi
// 1 - /agenda
// 2 - /ceps
// 3 - id
// Verifica se o ID está presente na URL
if (isset($uriParts[3]) && is_numeric($uriParts[3])) {
    $id = $uriParts[3];
}
//
// query params - end point = http://localhost/dsi/agenda/ceps?id=1
//  Verifica se o ID está presente na URL
// if (isset($_GET['id'])) {
//     $id = $_GET['id'];
// }    
//
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

// 
// exemplo arrya de objeto json
// [
//     {
//       "id": 18,
//       "cep": "15906-000",
//       "logradouro": "Rua Prof Paulao lazaro Mendes"
//       "bairro": "jardim micali"
//       "cidade" : "Taquaritinga"
//       "uf" : "sp"
//     }
//   ]

function getAll($conn)
{
    try {
        $stmt = $conn->query('SELECT * FROM ceps ORDER BY cep');        
        $response = $stmt->fetchAll(PDO::FETCH_ASSOC);       
        // $dataCep = getCepApi($response);

        header('Content-Type: application/json');
        echo json_encode($response);

    } catch (PDOException $e) {
        echo json_encode(['error' => $e->getMessage()]);
    }
}

function getById($conn, $id)
{
    if (isset($id) ){
        $stmt = $conn->prepare("SELECT * FROM ceps WHERE id = :id");
        $stmt->bindParam(':id', $id);
        $stmt->execute();
        $response = $stmt->fetch(PDO::FETCH_ASSOC);
        if ( $response){
            // $dataCep = getCepApi($response);
            header('Content-Type: application/json');
            echo json_encode($response);
        } else {
            echo json_encode(['error' => 'Registro não localizado']);
        }
        
    } else {
        echo json_encode(['error' => 'O id é obrigatório']);
    }
}

function post($conn)
{
    $data = json_decode(file_get_contents('php://input'), true);
    if (isset($data["cep"])) {
        $cep = $data['cep'];
        $logradouro = $data['logradouro'];
        $bairro = $data['bairro'];
        $cidade = $data['cidade'];
        $uf = $data['uf'];
        try {
            $stmt = $conn->prepare('INSERT INTO ceps (cep, logradouro, bairro, cidade, uf) VALUES (:cep, :logradouro, :bairro, :cidade, :uf)');
            $stmt->bindParam(':cep', $cep);
            $stmt->bindParam(':logradouro', $logradouro);
            $stmt->bindParam(':bairro', $bairro);
            $stmt->bindParam(':cidade', $cidade);
            $stmt->bindParam(':uf', $uf);
            $stmt->execute();
            $id = $conn->lastInsertId();
            echo json_encode(['id' => $id, 'cep' => $cep, 'logradouro' => $logradouro, 'bairro' => $bairro , 'cidade' => $cidade ]);
        } catch (PDOException $e) {
            echo json_encode(['error' => $e->getMessage()]);
        }
    } else {
        echo json_encode(['error' => 'O cep é obrigatório']);
    }
}

function put($conn, $id)
{
    $data = json_decode(file_get_contents('php://input'), true);
    if (isset($id)) {
        $cep = $data['cep'];
        $logradouro = $data['logradouro'];
        $bairro = $data['bairro'];
        $cidade = $data['cidade'];
        $uf = $data['uf'];
        try {
            $stmt = $conn->prepare('UPDATE ceps SET cep= :cep , logradouro= :logradouro , bairro = :bairro , cidade = :cidade , uf = :uf WHERE id = :id ');
            $stmt->bindParam(':id', $id);
            $stmt->bindParam(':cep', $cep);
            $stmt->bindParam(':logradouro', $logradouro);
            $stmt->bindParam(':bairro', $bairro);
            $stmt->bindParam(':cidade', $cidade);
            $stmt->bindParam(':uf', $uf);
            $stmt->execute();
            echo json_encode(['id' => $id, 'cep' => $cep, 'logradouro' => $logradouro, 'bairro' => $bairro , 'cidade' => $cidade ]);
        } catch (PDOException $e) {
            echo json_encode(['error' => $e->getMessage()]);
        }
    } else {
        echo json_encode(['error' => 'O id é obrigatório']);
    }
}

function delete($conn, $id)
{
    if (isset($id)) {
        try {
            $stmt = $conn->prepare('DELETE FROM ceps WHERE id = :id');
            $stmt->bindParam(':id', $id);
            $stmt->execute();
            echo json_encode(["message" => " Sucesso na exclusão !"]);
        } catch (PDOException $e) {
            echo json_encode(['error' => $e->getMessage()]);
        }
    } else {
        echo json_encode(['error' => 'O id é obrigatório']);
    }
}
