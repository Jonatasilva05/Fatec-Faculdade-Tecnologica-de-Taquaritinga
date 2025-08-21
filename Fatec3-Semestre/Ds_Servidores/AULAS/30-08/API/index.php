<?php session_start(); ?>
<?php 
    //cor's - liberação de acesso de qualquer endereco de IP
    header("Acces-Control-Allow-Origin: *");
    //json, UTF-8 para caractéres especiais do Português
    header("Content-Type: application/json; charset=UTF-8");

    $uri = parse_url($_SERVER['REQUEST_URI'], PHP_URL_PATH);

    //explode = quebra a linha do caractere que esta ali(array)
    //criando um array com o caminho da ri
    $patchs = explode('/', $uri);

    $endPoint = $_SERVER['PATH_INFO'];

    //capturar o verbo apirest ex.: GET / POST
    $requestMethod = $_SERVER['REQUEST_METHOD'];

    if ($requestMethod == "GET"){

        //prepara os dados no formato array para montagem do json
        $result = "{'mensagem':'ola mundo...'}";

        $jsonResult = json_encode($result);
        echo $jsonResult;
    }
?>