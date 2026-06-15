🚀 Guia Rápido: Adicionando PHP com Apache e Teste com index.php

Este passo vai complementar seu ambiente com PHP + Apache e um arquivo inicial para confirmar o funcionamento.

7. Criando o Diretório do Projeto

Crie uma pasta no seu sistema para armazenar os arquivos PHP:

mkdir sitephp
cd sitephp


Dentro dela, crie um arquivo index.php:

<?php
phpinfo();
?>


Esse arquivo mostra as informações do PHP, provando que está funcionando.

8. Subindo o Container do PHP + Apache

Agora vamos rodar o PHP com Apache mapeando a pasta sitephp:

docker run -d \
--name PHPAPACHE \
-h phpweb \
--network REDE1 \
-v "$PWD/sitephp":/var/www/html \
-p 8000:80 \
php:8.3-apache

Explicação:

--name PHPAPACHE → nome do container.

-h phpweb → hostname do servidor PHP.

--network REDE1 → conecta à mesma rede (pode falar com o banco depois).

-v "$PWD/sitephp":/var/www/html → monta a pasta local sitephp como raiz do Apache dentro do container.

-p 8000:80 → expõe o Apache na porta 8000.

php:8.3-apache → imagem oficial PHP 8.3 com Apache.

9. Testando no Navegador

Abra no navegador:

http://localhost:8000


Você verá a tela do phpinfo() confirmando que o PHP está rodando.

✅ Agora você tem:

MariaDB → banco de dados.

phpMyAdmin → gerenciador web em http://localhost:8080.

PHP + Apache → servidor web em http://localhost:8000 rodando seu código PHP.