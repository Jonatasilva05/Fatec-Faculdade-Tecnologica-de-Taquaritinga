<?php
//  rota para consulta todos os contatos
require '../database/config.php'; // importação do metodos do arquivo database.php

$uri = $_SERVER['REQUEST_URI'];

// captura o verbo sendo utilizado
$method = $_SERVER['REQUEST_METHOD'];

$uriParts = explode('/', trim($uri, '/')); // Divide a URI em partes e remove as barras extras
$id = 0 ;

// route params - end point = http://localhost/dsi/agenda/enderecos/1
// para funcionamento correto, necessario configurar arquivo .htacess, 
// indicando a pasta do index.php
// exemplo do $uriParts com a uri = "http://localhost/dsi/agenda/enderecos/1"
// 0 - /dsi
// 1 - /agenda
// 2 - /enderecos
// 3 - id
// Verifica se o ID está presente na URL
if (isset($uriParts[3]) && is_numeric($uriParts[3])) {
    $id = $uriParts[3];
}
//
// query params - end point = http://localhost/dsi/agenda/enderecos?id=1
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


// [
//     {
//       "id": 18,
//       "cep": "15906-000",
//       logradouro: "Rua Prof Paulao lazaro Mendes"
//       bairro: "jardim micali"
//       cidade : Taquaritinga
//       uf : sp
//       "numero": "2241",
//       "complemento": "casa do COMUNISTA"
//     }
//   ]

function getAll($conn)
{
    try {
        $stmt = $conn->query('SELECT * FROM enderecos ORDER BY cep');        
        $response = $stmt->fetchAll(PDO::FETCH_ASSOC);       
        $dataCep = getCepApi($response);

        header('Content-Type: application/json');
        echo json_encode($dataCep);

    } catch (PDOException $e) {
        echo json_encode(['error' => $e->getMessage()]);
    }
}

function getById($conn, $id)
{
    if (isset($id) ){
        $stmt = $conn->prepare("SELECT * FROM enderecos WHERE id = :id");
        $stmt->bindParam(':id', $id);
        $stmt->execute();
        $response = $stmt->fetch(PDO::FETCH_ASSOC);
        if ( $response){
            $dataCep = getCepApi($response);
            header('Content-Type: application/json');
            echo json_encode($dataCep);
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
        $numero = $data['numero'];
        $complemento = $data['complemento'];
        try {
            $stmt = $conn->prepare('INSERT INTO enderecos (cep,numero,complemento) VALUES (:cep, :numero, :complemento)');
            $stmt->bindParam(':cep', $cep);
            $stmt->bindParam(':numero', $numero);
            $stmt->bindParam(':complemento', $complemento);
            $stmt->execute();
            $id = $conn->lastInsertId();
            echo json_encode(['id' => $id, 'cep' => $cep, 'numero' => $numero, 'complemento' => $complemento]);
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
        $numero = $data['numero'];
        $complemento = $data['complemento'];
        try {
            $stmt = $conn->prepare('UPDATE enderecos SET cep= :cep , numero= :numero ,complemento = :complemento WHERE id = :id ');
            $stmt->bindParam(':id', $id);
            $stmt->bindParam(':cep', $cep);
            $stmt->bindParam(':numero', $numero);
            $stmt->bindParam(':complemento', $complemento);
            $stmt->execute();
            echo json_encode(['id' => $id, 'nome' => $cep, 'numero' => $numero]);
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
            $stmt = $conn->prepare('DELETE FROM enderecos WHERE id = :id');
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

function getCepApi0( $response ){
    // Fazer uma chamada à API pública de CEP para obter os dados adicionais
    foreach ($response as $endereco) {

        $cep = preg_replace('/[^0-9]/', '', $endereco['cep']); // Remove caracteres não numéricos do CEP
        $cepApiUrl = "https://brasilapi.com.br/api/cep/v1/$cep";
        $cepData = file_get_contents($cepApiUrl);
        $cepDetails = json_decode($cepData, true);   
        // Combinar os dados da API com os dados do banco de dados
        if ($cepDetails && !isset($cepDetails['erro'])) {
            $endereco['logradouro'] = $cepDetails['street'] ?? null;
            $endereco['bairro'] = $cepDetails['neighborhood'] ?? null;
            $endereco['cidade'] = $cepDetails['city'] ?? null;
            $endereco['uf'] = $cepDetails['state'] ?? null;
        }
      }   
    return $response ;
}

function getCepApi($enderecos)
{
    // Verifica se estamos lidando com um único endereço ou uma lista de endereços
    $enderecos = is_assoc($enderecos) ? [$enderecos] : $enderecos; // Transforma em uma lista se for um único item

    // Itera sobre cada endereço para fazer a chamada à API pública de CEP
    foreach ($enderecos as &$endereco) { // Usamos `&$endereco` para modificar o array original diretamente
        $cep = preg_replace('/[^0-9]/', '', $endereco['cep']); // Remove caracteres não numéricos do CEP
        $cepApiUrl = "https://brasilapi.com.br/api/cep/v1/$cep";

        // Fazer a chamada à API pública e obter os dados do CEP
        $cepData = @file_get_contents($cepApiUrl); // Usar `@` para suprimir erros de warning
        $cepDetails = $cepData ? json_decode($cepData, true) : null; // Verifica se a resposta da API é válida

        // Combina os dados da API com os dados do banco de dados, se a resposta da API for válida
        if ($cepDetails && !isset($cepDetails['erro'])) {
            $endereco['logradouro'] = $cepDetails['street'] ?? null;
            $endereco['bairro'] = $cepDetails['neighborhood'] ?? null;
            $endereco['cidade'] = $cepDetails['city'] ?? null;
            $endereco['uf'] = $cepDetails['state'] ?? null;
        } else {
            // Se o CEP for inválido ou não existir, definir valores padrão
            $endereco['logradouro'] = 'CEP não encontrado';
            $endereco['bairro'] = 'CEP não encontrado';
            $endereco['cidade'] = 'CEP não encontrado';
            $endereco['uf'] = 'CEP não encontrado';
        }
    }

    return count($enderecos) === 1 ? $enderecos[0] : $enderecos; // Retorna um único endereço ou uma lista de endereços
}

// Função auxiliar para verificar se um array é associativo
function is_assoc($array)
{
    return array_keys($array) !== range(0, count($array) - 1);
}
