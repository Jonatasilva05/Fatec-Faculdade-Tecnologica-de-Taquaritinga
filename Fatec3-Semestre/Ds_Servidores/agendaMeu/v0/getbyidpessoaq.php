<?php
// Rota para consulta de contatos
require 'database.php'; // Importação dos métodos do arquivo database.php

// Obtém a URL atual e faz o parse para encontrar o ID na rota
$requestUri = $_SERVER['REQUEST_URI'];
$uriParts = explode('/', trim($requestUri, '/')); // Divide a URI em partes e remove as barras extras

// Verifica se o ID está presente na URL
if (isset($uriParts[4]) && is_numeric($uriParts[4])) {
    $id = $uriParts[4];

    try {
        // Prepara e executa a query para buscar a pessoa pelo ID
        $stmt = $conn->prepare("SELECT * FROM pessoas WHERE id = :id");
        $stmt->bindParam(':id', $id, PDO::PARAM_INT);
        $stmt->execute();
        $pessoas = $stmt->fetchAll(PDO::FETCH_ASSOC);

        // Define o tipo de conteúdo como JSON e retorna o resultado
        header('Content-Type: application/json');
        echo json_encode($pessoas);
    } catch (PDOException $e) {
        // Retorna o erro em formato JSON
        echo json_encode(['error' => $e->getMessage()]);
    }
} else {
    // Retorna erro caso o ID não tenha sido enviado corretamente
    echo json_encode(['error' => 'O id é obrigatório e deve ser um número']);
}


// Explicação:
// Captura do ID na URL: A variável $_SERVER['REQUEST_URI'] captura toda a URI da requisição. A função explode('/', trim($requestUri, '/')) divide essa URI em partes, com o ID sendo a segunda parte (índice [1]).

// Por exemplo, se a URL for http://localhost/pessoa_get.php/1, o array explode vai gerar algo como ['pessoa_get.php', '1'].
// O valor 1 (que está na posição [1]) será o ID.
// Verificação do ID: Verificamos se a segunda parte da URL existe e se é um número (is_numeric).

// Execução da query: A consulta ao banco de dados é feita com o ID extraído da URL, assim como no seu código original.

// Erro quando o ID não é fornecido: Caso o ID não seja passado na URL ou não seja um número válido, retornamos um erro.

// Teste:
// Agora, a API pode ser acessada por uma URL do tipo:

// http://localhost/pessoa_get.php/1
// http://localhost/pessoa_get.php/2
// Isso simula um comportamento semelhante ao de frameworks modernos que utilizam rotas dinâmicas com parâmetros diretamente na URL.

// Se você estiver rodando o PHP via Apache ou outro servidor com mod_rewrite configurado, essa estrutura pode ser facilmente adaptada para se comportar como um roteamento mais avançado.
//
// http://localhost/dsi/agenda/v0/getbyidpessoaq.php/1