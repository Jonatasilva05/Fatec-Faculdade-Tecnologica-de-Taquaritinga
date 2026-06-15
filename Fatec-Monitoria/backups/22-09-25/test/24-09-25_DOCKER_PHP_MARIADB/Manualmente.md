# Parte 1: A Abordagem Manual com docker run
Nesta seção, vamos construir nosso ambiente peça por peça para entender o papel de cada componente.

## Passo 1: A Rede Docker
Para que os contêineres do PHP e do MySQL possam se comunicar de forma segura e pelo nome, criamos uma rede virtual privada para eles.


Para criar uma rede privada execute:

```Bash
docker network create minha-rede-php
```


## Passo 2: O Banco de Dados (MySQL) 

Agora, subimos o contêiner do banco de dados, conectando-o à nossa rede e criando um volume para persistir os dados.

```Bash
docker run -d \
--name mysql-db \
--network minha-rede-php \
-e MYSQL_ROOT_PASSWORD=sua_senha_forte \
-e MYSQL_DATABASE=meu_banco \
-v mysql-data:/var/lib/mysql \
mysql:8.0
```

### O que cada linha faz?

- --name mysql-db: Dá um nome ao contêiner, que será usado pelo PHP para se conectar.

- --network minha-rede-php: Conecta o contêiner à rede que criamos.

- -e VAR=valor: Define variáveis de ambiente para configurar o MySQL (senha e nome do banco inicial).

- -v mysql-data:/var/lib/mysql: A parte mais importante! Cria um volume chamado mysql-data em sua máquina e o espelha na pasta onde o MySQL guarda os dados. Isso garante que você não perca seus dados mesmo que o contêiner seja removido.

## Passo 3: O Servidor Web (PHP + Apache)
Primeiro, crie a pasta que conterá os arquivos do seu site.

```Bash
mkdir pasta_do_site
cd pasta_do_site
```

Agora, de dentro da pasta_do_site, execute o comando para criar o contêiner do PHP.

```Bash
docker run -d \
-p 8080:80 \
--name meu-servidor-php \
--network minha-rede-php \
-v "$(pwd)":/var/www/html \
php:8.2-apache
```

### O que cada linha faz?

- -p 8080:80: Mapeia a porta 8080 do seu computador para a porta 80 do contêiner. Você acessará o site em http://localhost:8080.

- -v "$(pwd)":/var/www/html: Espelha a sua pasta atual (pasta_do_site) para dentro do contêiner. Qualquer alteração nos arquivos é refletida instantaneamente.

## Passo 4: Instalar a Extensão e Testar
A imagem padrão do PHP não vem com a extensão para MySQL. Precisamos instalá-la manualmente.

Entre no contêiner PHP:

```Bash
docker exec -it meu-servidor-php bash
```

Dentro do contêiner, execute:

```Bash
# Instala a extensão
docker-php-ext-install pdo_mysql
```

```Bash
# Reinicia o Apache para carregar a extensão
apache2ctl restart
```

Saia do contêiner digitando exit.