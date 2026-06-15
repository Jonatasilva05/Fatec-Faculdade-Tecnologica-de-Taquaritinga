<?php

    $nomepagina = "MagodosPcs - Inicio";

    $css = [
        "../../css/estilos.css",
        "../../css/alternativo.css",
    ];

    # o for sempre sera 3 "categoria"
    #primeira variavel sempre sera de controle e sempre recebera o valor de 0
    #segunda variavel sera quando ele ira parar no nosso caso quando chegar em 2 ele para mas o 0 sempre sera menor entao ele nunca ira parar por isso temos a terceira variavel
    #terceira variavel ira implementar mais um valor ao numero atual, ou seja sera a variavel $g que atualmente ela é igual a 0 entao depois disso ela sera somada com ++, no final ele sera 0+1, 1+1 e assim por diante ate ser 2 e parar no 2 que foi como configuramos ele
    // for( $g=0; $g<2; $g++) {
    //     echo $css[$g];
    // }

    #funciona igual mas de maneira mais curta
    // $quantItens = count($css);
    // for( $g=0; $g<$quantItens; $g++) {
    //     echo $css[$g];
    // }

    for ( $g=0; $g<count($css); $g++) {
        echo $css[$g];
    }

?>

<!DOCTYPE html>
<html lang="pt-br">

    <!-- CHAMANDO O head.php QUE ESTA DENTRO DE VIEWS -->
    <?php include_once __DIR__ . "/../views/head.php"; ?>
    
<body>

    <?php 
    
        include_once __DIR__ . "/../views/header.php"; 

        include_once __DIR__ . "/../views/paginaInicial.php";

        include_once __DIR__ . "/../views/footer.php"
    
    ?>

</body>
</html>