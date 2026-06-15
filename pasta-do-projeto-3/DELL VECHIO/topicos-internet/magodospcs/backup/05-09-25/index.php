<?php

    # Recebe todas as URI que vem do servidor, (requisições que vem do servidor), incluindo argumentos
    $uritotal = $_SERVER["REQUEST_URI"];


    # Função do PHP para dividir a uri em partes
    $partes = parse_url($uritotal);


    # Recebe somente a parte da uri, basicamente um filtro evitando que os argumentos(query) apareça
    $urirefinada = $partes["path"];


    # Refina a uri retirando barras no inicio e no fim. Trim serve para retirar/aparar o selecionado
    $urirefinada = trim($urirefinada, "/");


    # Divide a uri a partir da barra, criando um array
    $divisaouri = explode("/", $urirefinada);


    # Pega somente o string na posição 0 do array
    $uri = $divisaouri[0];


    # Cria o array associativo de rotas
    $rotas = [
        "" => "inicioController", 
        "quemsomos" => "quemsomosController",
        "contato" => "contatoController"
    ];


    # Verifica se o uri existe como chave no array rotas
    if(array_key_exists($uri, $rotas)){

        # Define o controlador
        $controlador = $rotas[$uri];

        # Inclui o arquivo php do controlador
        include __DIR__ . "/app/controllers/$controlador.php";
    }
    else{
        # Se não encontrar a chave
        echo "nao existe essa chave";
    }

?>