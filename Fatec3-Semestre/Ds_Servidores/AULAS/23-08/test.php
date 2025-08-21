<?php 
    $name = $_POST['name'];
    $idade = $_POST['idade'];
    $email = $_POST['mail'];

?>


<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>

    <p>
        Seu nome é: <?php echo $name ?> , Você tem <?php echo $idade ?> anos de idade, Seu Email é: <?php echo $email ?> ;
    </p>    
    
</body>
</html>