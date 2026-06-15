<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title><?= $nomepagina ?></title>
    
    <?php for($g=0; $g<count($css); $g++): ?>
        <link rel="stylesheet" href="<?= $css[$g] ?>">
    <?php endfor; ?>
    
    <!-- Esse é um dos metodos mas nao é totalmente necessario e tambem nem tanto ultilizado -->
    <?php 

        for($g=0; $g<count($css); $g++) {
            #para nao colocar dessa maneira que talvez confunda 
            // echo "<link rel='stylesheet' href='$css{[$g]}'>";

            // faça dessa maneira
            $posicao = $css[$g];
            echo "<link rel='stylesheet' href='$posicao'>";
        }

    ?>
</head>