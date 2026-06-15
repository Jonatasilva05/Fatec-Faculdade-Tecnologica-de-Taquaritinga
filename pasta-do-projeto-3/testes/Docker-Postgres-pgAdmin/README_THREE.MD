🐳 Ambiente PHP + PostgreSQL + Nginx com Docker Compose

Este projeto demonstra como configurar um ambiente completo com PHP, PostgreSQL e Nginx, totalmente isolado e gerenciado por Docker Compose.
Tudo roda em containers separados, refletindo um ambiente de produção moderno e seguro.

📦 Pré-requisitos

Antes de começar, verifique se você possui instalado em sua máquina:

Docker

Docker Compose

🧱 Passo 1: Criar Rede e Volume (opcional)

Você pode criar manualmente uma rede e volume, embora o Docker Compose também possa gerenciá-los automaticamente.

# Criar uma rede
docker network create jonatas

# (Opcional) Criar um volume para persistência de dados
docker volume create meu-volume

🐘 Passo 2: Subir Containers Manualmente (Opcional)

Antes de usar o docker-compose, você pode testar os containers manualmente.

Container PostgreSQL
docker run --name meuPost \
  --network jonatas \
  -e POSTGRES_PASSWORD=senha123 \
  -p 5432:5432 \
  -d postgres:13.22-alpine3.22

Container PgAdmin (Interface Web para Postgres)
docker run --name meuPgAdmin \
  --network jonatas \
  -p 8080:80 \
  -e "PGADMIN_DEFAULT_EMAIL=admin@teste.com" \
  -e "PGADMIN_DEFAULT_PASSWORD=senha123" \
  -d dpage/pgadmin4


Após cerca de 10–15 segundos, acesse:

🔗 http://localhost:8080

Login: admin@teste.com

Senha: senha123

Conexão com o banco dentro do pgAdmin:

Host name/address: meuPost

Port: 5432

Maintenance database: postgres

Username: postgres

Password: senha123

Se a conexão for bem-sucedida, seu container do Postgres está funcionando corretamente. 🎉

🧰 Passo 3: Estrutura do Projeto

Crie a seguinte estrutura de diretórios:

teste-php-pg/
├── docker-compose.yml
├── nginx.conf
└── src/
    ├── index.html
    └── conectar.php

⚙️ Passo 4: Arquivos do Projeto
🧾 docker-compose.yml
version: '3.8'

services:
  db:
    image: postgres:13-alpine
    container_name: meuPost-compose
    restart: always
    environment:
      POSTGRES_PASSWORD: senha123
    ports:
      - "5432:5432"
    volumes:
      - dados-postgres:/var/lib/postgresql/data
    networks:
      - rede-app

  nginx:
    image: nginx:1.21-alpine
    container_name: meuNginx-compose
    restart: always
    ports:
      - "8000:80"
    volumes:
      - ./src:/var/www/html
      - ./nginx.conf:/etc/nginx/conf.d/default.conf
    networks:
      - rede-app
    depends_on:
      - php

  php:
    image: php:8.1-fpm-alpine
    container_name: meuPHP-compose
    restart: always
    volumes:
      - ./src:/var/www/html
    networks:
      - rede-app
    depends_on:
      - db

networks:
  rede-app:
    driver: bridge

volumes:
  dados-postgres:
    driver: local

🧾 nginx.conf
server {
    listen 80;
    index index.php index.html;
    server_name localhost;
    root /var/www/html;
    
    location / {
        try_files $uri $uri/ /index.php?$query_string;
    }

    location ~ \.php$ {
        try_files $uri =404;
        fastcgi_split_path_info ^(.+\.php)(/.+)$;
        fastcgi_pass php:9000;
        fastcgi_index index.php;
        include fastcgi_params;
        fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
        fastcgi_param PATH_INFO $fastcgi_path_info;
    }
}

🧾 src/index.html
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Teste Postgres com PHP (Docker)</title>
    <style>
        body { font-family: sans-serif; margin: 20px; background: #f4f4f4; }
        .container { max-width: 600px; margin: auto; padding: 20px; background: #fff; border-radius: 8px; }
        input[type="text"] { width: 95%; padding: 8px; margin-bottom: 10px; }
    </style>
</head>
<body>
    <div class="container">
        <h2>Testar Conexão e Inserir Dados (Docker)</h2>
        <form action="conectar.php" method="post">
            <label for="nome">Seu Nome:</label>
            <input type="text" id="nome" name="nome" required>
            <input type="submit" value="Testar e Salvar">
        </form>
    </div>
</body>
</html>

🧾 src/conectar.php
<?php
$host = 'db';
$port = '5432';
$db = 'postgres';
$user = 'postgres';
$pass = 'senha123';

$dsn = "pgsql:host=$host;port=$port;dbname=$db;user=$user;password=$pass";
?>
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Resultado da Conexão</title>
    <style>
        body { font-family: sans-serif; margin: 20px; background: #f4f4f4; }
        .container { max-width: 600px; margin: auto; padding: 20px; background: #fff; border-radius: 8px; }
        .success { color: green; }
        .error { color: red; }
    </style>
</head>
<body>
<div class="container">
<?php
try {
    $pdo = new PDO($dsn);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    echo "<h1 class='success'>Conexão com PostgreSQL (Docker) bem-sucedida!</h1>";

    $pdo->exec("CREATE TABLE IF NOT EXISTS visitantes (
                    id SERIAL PRIMARY KEY,
                    nome VARCHAR(100) NOT NULL,
                    data_visita TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )");

    if ($_SERVER['REQUEST_METHOD'] == 'POST' && !empty($_POST['nome'])) {
        $nome = htmlspecialchars($_POST['nome']);
        $stmt = $pdo->prepare("INSERT INTO visitantes (nome) VALUES (?)");
        $stmt->execute([$nome]);
        echo "<p>Usuário '<strong>{$nome}</strong>' inserido com sucesso!</p>";
    }

    echo "<h3>Visitantes Registrados no Banco:</h3>";
    $stmt = $pdo->query("SELECT nome, data_visita FROM visitantes ORDER BY data_visita DESC");
    echo "<ul>";
    while ($row = $stmt->fetch(PDO::FETCH_ASSOC)) {
        echo "<li>" . $row['nome'] . " (em " . $row['data_visita'] . ")</li>";
    }
    echo "</ul>";

} catch (PDOException $e) {
    echo "<h1 class='error'>Falha na conexão!</h1>";
    echo "<p><strong>Erro:</strong> " . $e->getMessage() . "</p>";
}
?>
<br><a href="index.html">Voltar ao formulário</a>
</div>
</body>
</html>

🚀 Passo 5: Subir o Ambiente

Na raiz do projeto, execute:

docker-compose up -d --build

🌐 Passo 6: Testar no Navegador

Acesse:
👉 http://localhost:8000

Preencha o campo de nome.

Clique em “Testar e Salvar”.

Se a página mostrar “Conexão com PostgreSQL (Docker) bem-sucedida!”, tudo funcionou perfeitamente. 🎉

🧹 Parar e Limpar Containers
docker-compose down


Remover também o volume (dados do banco):

docker-compose down -v

🧠 Comandos Úteis do Docker
Comando	Descrição
docker ps	Lista containers em execução
docker-compose ps	Mostra o status dos serviços do compose
docker-compose logs -f nginx	Exibe logs do Nginx em tempo real
docker exec -it meuPHP-compose sh	Acessa o shell do container PHP
docker exec -it meuPost-compose psql -U postgres	Acessa o PostgreSQL direto no container
docker network ls	Lista as redes criadas
docker volume ls	Lista volumes locais
docker system prune -f	Remove containers, imagens e redes não utilizados
docker-compose build --no-cache	Reconstrói os containers sem usar cache
💥 Troubleshooting (Erros Comuns e Soluções)
⚠️ 1. Erro de Conexão no PHP:

“SQLSTATE[08006] [7] could not connect to server”

✅ Soluções possíveis:

O nome do host em conectar.php deve ser db (nome do serviço no docker-compose.yml, não localhost).

Confirme se o Postgres está rodando:

docker-compose ps


Tente reiniciar tudo:

docker-compose down && docker-compose up -d

⚠️ 2. Erro de Permissão nos Arquivos PHP

“Permission denied” ou erro 403 no Nginx.

✅ Soluções possíveis:

Verifique as permissões da pasta src/:

chmod -R 755 src/


No Windows, garanta que o volume está sendo compartilhado corretamente com o Docker Desktop.

⚠️ 3. Portas em Uso

“Bind for 0.0.0.0:5432 failed: port is already allocated”

✅ Soluções possíveis:

Feche containers antigos que usam a mesma porta:

docker ps
docker stop <id_do_container>


Ou altere as portas no docker-compose.yml:

ports:
  - "15432:5432"

⚠️ 4. PgAdmin Não Conecta ao Postgres

✅ Soluções possíveis:

Use o nome do container (meuPost-compose ou db) como host.

Espere 10–15 segundos após subir os containers — o Postgres pode demorar um pouco para inicializar.

⚠️ 5. Erro de Comunicação entre Containers

✅ Soluções possíveis:

Certifique-se de que todos estão na mesma rede:

docker network inspect teste-php-pg_rede-app


Se algum container não estiver listado, reconstrua:

docker-compose down && docker-compose up -d

✅ Resultado Final

Você agora possui um ambiente completo e funcional com:

🐘 PostgreSQL 13

🐍 PHP 8.1 FPM

🌐 Nginx (alpine)

🧩 Tudo orquestrado via Docker Compose

💡 Ideal para estudos, testes de integração e desenvolvimento local seguro.
Se quiser evoluir este projeto, adicione PHPMyAdmin, Redis, ou pgAdmin via Compose também!