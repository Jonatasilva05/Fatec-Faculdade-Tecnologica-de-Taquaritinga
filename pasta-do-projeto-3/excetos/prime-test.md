Guia Completo: Do Zero ao Profissional com Docker, PHP e MySQL
Este guia é um passo a passo completo para criar um ambiente de desenvolvimento local para aplicações PHP e MySQL usando Docker. Começaremos com os comandos manuais para entender cada conceito e evoluiremos para uma abordagem profissional e portátil usando Docker Compose.

Índice
Parte 1: A Abordagem Manual com docker run

Parte 2: Criando uma Aplicação de Cadastro (CRUD Básico)

Parte 3: Gerenciando o Ciclo de Vida dos Contêineres

Parte 4: Backup e Restauração do Banco de Dados

Parte 5: A Abordagem Profissional com Docker Compose

Parte 1: A Abordagem Manual com docker run
Nesta seção, vamos construir nosso ambiente peça por peça para entender o papel de cada componente.

Passo 1: A Rede Docker
Para que os contêineres do PHP e do MySQL possam se comunicar de forma segura e pelo nome, criamos uma rede virtual privada para eles.

Bash

docker network create minha-rede-php
Passo 2: O Banco de Dados (MySQL)
Agora, subimos o contêiner do banco de dados, conectando-o à nossa rede e criando um volume para persistir os dados.

Bash

docker run -d \
--name mysql-db \
--network minha-rede-php \
-e MYSQL_ROOT_PASSWORD=sua_senha_forte \
-e MYSQL_DATABASE=meu_banco \
-v mysql-data:/var/lib/mysql \
mysql:8.0
O que cada linha faz?

--name mysql-db: Dá um nome ao contêiner, que será usado pelo PHP para se conectar.

--network minha-rede-php: Conecta o contêiner à rede que criamos.

-e VAR=valor: Define variáveis de ambiente para configurar o MySQL (senha e nome do banco inicial).

-v mysql-data:/var/lib/mysql: A parte mais importante! Cria um volume chamado mysql-data em sua máquina e o espelha na pasta onde o MySQL guarda os dados. Isso garante que você não perca seus dados mesmo que o contêiner seja removido.

Passo 3: O Servidor Web (PHP + Apache)
Primeiro, crie a pasta que conterá os arquivos do seu site.

Bash

mkdir pasta_do_site
cd pasta_do_site
Agora, de dentro da pasta_do_site, execute o comando para criar o contêiner do PHP.

Bash

docker run -d \
-p 8080:80 \
--name meu-servidor-php \
--network minha-rede-php \
-v "$(pwd)":/var/www/html \
php:8.2-apache
O que cada linha faz?

-p 8080:80: Mapeia a porta 8080 do seu computador para a porta 80 do contêiner. Você acessará o site em http://localhost:8080.

-v "$(pwd)":/var/www/html: Espelha a sua pasta atual (pasta_do_site) para dentro do contêiner. Qualquer alteração nos arquivos é refletida instantaneamente.

Passo 4: Instalar a Extensão e Testar
A imagem padrão do PHP não vem com a extensão para MySQL. Precisamos instalá-la manualmente.

Entre no contêiner PHP:

Bash

docker exec -it meu-servidor-php bash
Dentro do contêiner, execute:

Bash

# Instala a extensão
docker-php-ext-install pdo_mysql

# Reinicia o Apache para carregar a extensão
apache2ctl restart
Saia do contêiner digitando exit.

Parte 2: Criando uma Aplicação de Cadastro (CRUD Básico)
Agora que o ambiente está de pé, vamos criar uma aplicação simples para cadastrar e listar usuários. Todos os arquivos a seguir devem ser criados dentro da pasta_do_site.

Passo 1: Preparar a Tabela no Banco
Acesse o contêiner do MySQL:

Bash

docker exec -it mysql-db mysql -u root -p
(Será solicitada a senha sua_senha_forte)

Dentro do MySQL, crie a tabela:

SQL

USE meu_banco;

CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

EXIT;
Passo 2: Arquivos da Aplicação
Crie os seguintes arquivos dentro de pasta_do_site:

1. conexao.php (Centraliza a conexão com o banco)

PHP

<?php
$host = 'mysql-db';
$db   = 'meu_banco';
$user = 'root';
$pass = 'sua_senha_forte'; // Lembre-se de usar a sua senha!
$charset = 'utf8mb4';

$dsn = "mysql:host=$host;dbname=$db;charset=$charset";
$options = [
    PDO::ATTR_ERRMODE            => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
    PDO::ATTR_EMULATE_PREPARES   => false,
];

try {
     $pdo = new PDO($dsn, $user, $pass, $options);
} catch (\PDOException $e) {
     throw new \PDOException($e->getMessage(), (int)$e->getCode());
}
?>
2. index.php (Página inicial com menu)

PHP

<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Meu Primeiro CRUD</title>
</head>
<body>
    <h1>Bem-vindo ao Sistema de Cadastro</h1>
    <a href="formulario.php">Cadastrar Novo Usuário</a>
    <a href="listar.php">Ver Usuários Cadastrados</a>
</body>
</html>
3. formulario.php (Formulário para inserir dados)

PHP

<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Cadastro de Usuário</title>
</head>
<body>
    <form action="salvar.php" method="POST">
        <h2>Formulário de Cadastro</h2>
        <label for="nome">Nome:</label>
        <input type="text" id="nome" name="nome" required>
        <br><br>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
        <br><br>
        <input type="submit" value="Cadastrar">
    </form>
</body>
</html>
4. salvar.php (Script que recebe os dados e salva no banco)

PHP

<?php
include 'conexao.php';

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $nome = $_POST['nome'];
    $email = $_POST['email'];

    try {
        $sql = "INSERT INTO usuarios (nome, email) VALUES (:nome, :email)";
        $stmt = $pdo->prepare($sql);
        $stmt->execute(['nome' => $nome, 'email' => $email]);

        echo "<h1>Usuário cadastrado com sucesso!</h1>";
        echo "<a href='formulario.php'>Cadastrar outro</a> | <a href='listar.php'>Ver todos</a>";

    } catch (PDOException $e) {
        die("Erro ao cadastrar usuário: " . $e->getMessage());
    }
}
?>
5. listar.php (Página que exibe todos os usuários cadastrados)

PHP

<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Lista de Usuários</title>
</head>
<body>
    <h1>Usuários Cadastrados</h1>
    <a href="index.php">Voltar para o Início</a>
    <table border="1" width="100%">
        <thead>
            <tr>
                <th>ID</th>
                <th>Nome</th>
                <th>Email</th>
                <th>Data de Cadastro</th>
            </tr>
        </thead>
        <tbody>
            <?php
            include 'conexao.php';
            $stmt = $pdo->query("SELECT id, nome, email, data_cadastro FROM usuarios ORDER BY id DESC");
            while ($usuario = $stmt->fetch()) {
                echo "<tr>";
                echo "<td>" . htmlspecialchars($usuario['id']) . "</td>";
                echo "<td>" . htmlspecialchars($usuario['nome']) . "</td>";
                echo "<td>" . htmlspecialchars($usuario['email']) . "</td>";
                echo "<td>" . htmlspecialchars($usuario['data_cadastro']) . "</td>";
                echo "</tr>";
            }
            ?>
        </tbody>
    </table>
</body>
</html>
Parte 3: Gerenciando o Ciclo de Vida dos Contêineres
Como Parar e Ligar
Bash

# Para parar os contêineres
docker stop meu-servidor-php mysql-db

# Para ligá-los novamente
docker start mysql-db meu-servidor-php
Como Remover (Apagar)
Lembre-se: Um contêiner precisa estar parado para ser removido.

Bash

# 1. Pare o contêiner
docker stop meu-servidor-php

# 2. Remova o contêiner
docker rm meu-servidor-php
E os meus dados? Você NÃO perde seus dados do site (arquivos PHP) nem do banco, pois eles estão guardados em volumes na sua máquina, e não dentro do contêiner descartável.

Parte 4: Backup e Restauração do Banco de Dados
Exportar (Fazer Backup)
Use o mysqldump para criar um arquivo .sql com toda a estrutura e dados do seu banco.

Bash

docker exec mysql-db mysqldump -u root -p'sua_senha_forte' meu_banco > backup_do_banco.sql
Este comando cria o arquivo backup_do_banco.sql na sua pasta atual.

Importar (Restaurar um Backup)
Use o cat e um pipe para "empurrar" o conteúdo do seu arquivo .sql para dentro do banco.

Bash

cat backup_do_banco.sql | docker exec -i mysql-db mysql -u root -p'sua_senha_forte' meu_banco
Parte 5: A Abordagem Profissional com Docker Compose
Escrever comandos docker run longos é cansativo e sujeito a erros. O Docker Compose permite definir todo o seu ambiente em um único arquivo docker-compose.yml.

Passo 1: Limpe o Ambiente Anterior
Pare e remova os contêineres que criamos manualmente para evitar conflitos.

Bash

docker stop meu-servidor-php mysql-db
docker rm meu-servidor-php mysql-db
Passo 2: Crie o arquivo docker-compose.yml
Na raiz do seu projeto (fora da pasta_do_site), crie o arquivo docker-compose.yml:

YAML

version: '3.8'

services:
  php:
    image: php:8.2-apache
    container_name: meu-servidor-php
    ports:
      - "8080:80"
    volumes:
      - ./pasta_do_site:/var/www/html
      # Adicionaremos um Dockerfile em breve para a extensão
    networks:
      - minha-rede-php
    depends_on:
      - mysql

  mysql:
    image: mysql:8.0
    container_name: mysql-db
    environment:
      MYSQL_ROOT_PASSWORD: sua_senha_forte
      MYSQL_DATABASE: meu_banco
    volumes:
      - mysql-data:/var/lib/mysql
      # Para popular o banco na primeira inicialização (opcional)
      - ./mysql-init:/docker-entrypoint-initdb.d
    networks:
      - minha-rede-php

networks:
  minha-rede-php:

volumes:
  mysql-data:
Passo 3: Automatize a Instalação da Extensão (Opcional, mas recomendado)
Para não ter que instalar o pdo_mysql manualmente toda vez, crie um arquivo Dockerfile na raiz do seu projeto.

Dockerfile

Dockerfile

FROM php:8.2-apache
RUN docker-php-ext-install pdo_mysql
Agora, ajuste o serviço php no seu docker-compose.yml para usar este arquivo:

YAML

# ...
services:
  php:
    build: . # <--- Mude 'image' para 'build'
    container_name: meu-servidor-php
#... o resto continua igual
Passo 4: O Fluxo de Trabalho com Git e Docker Compose
O que vai para o GitHub?

O arquivo docker-compose.yml

O Dockerfile

Toda a pasta_do_site com seu código PHP

O arquivo de backup backup_do_banco.sql (geralmente dentro de uma pasta como mysql-init)

Como rodar o projeto em outra máquina?

Bash

# Clone o projeto
git clone https://github.com/seu-usuario/seu-projeto.git
cd seu-projeto

# Suba todo o ambiente com um único comando
docker-compose up -d --build

# Para desligar tudo
docker-compose down
Este fluxo de trabalho torna seu projeto 100% portátil e fácil de configurar em qualquer lugar.