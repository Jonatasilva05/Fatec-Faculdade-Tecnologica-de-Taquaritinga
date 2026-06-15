# 🚀 Guia Rápido: Docker com MariaDB, PHP, phpMyAdmin e Apache  

Este guia ensina, de forma simples e prática, como configurar um ambiente básico com **MariaDB**, **PHP**, **phpMyAdmin** e **Apache** usando Docker.  

---

## 1. Criando a Rede do Projeto  

Primeiro, vamos criar uma rede Docker para conectar nossos containers:  

```bash
docker network create REDE1
```

Para confirmar a criação:  

```bash
docker network ls
```

---

## 2. Criando o Volume para os Dados  

Crie um volume para persistir os dados do banco:  

```bash
docker volume create VOL1
```

Confirme:  

```bash
docker volume ls
```

---

## 3. Subindo o Container do MariaDB  

Execute o MariaDB:  

```bash
docker run -d --name MARIADB -v VOL1:/var/lib/mysql -h db --network REDE1 --env MARIADB_USER=user --env MARIADB_PASSWORD=senha12345 --env MARIADB_ROOT_PASSWORD=senharoot123 mariadb:latest
```

---

## 4. Subindo o Container do phpMyAdmin  

Execute o phpMyAdmin:  

```bash
docker run -d --name MYADMIN -h myadmin --network REDE1 -e PMA_HOST=db -p 8080:80 phpmyadmin:latest
```

Acesse no navegador:  

```
http://localhost:8080
```

- **Servidor:** `db`  
- **Usuário:** `user` (ou `root`)  
- **Senha:** `senha12345` (ou `senharoot123`)  

---

## 5. Criando o Diretório do Projeto PHP  

Crie uma pasta local para seus arquivos PHP:  

```bash
mkdir sitephp
cd sitephp
```

Crie o arquivo `index.php`:  

```php
<?php
phpinfo();
?>
```

---

## 6. Subindo o Container do PHP + Apache  

Agora vamos rodar o PHP com Apache, mapeando a pasta `sitephp`:  

```bash
docker run -d --name PHPAPACHE -h phpweb --network REDE1 -v "$PWD/sitephp":/var/www/html -p 8000:80 php:8.3-apache
```

---

## 7. Testando o Servidor  

Abra no navegador:  

```
http://localhost:8000
```

Você verá a tela do `phpinfo()`, confirmando que o PHP está rodando com Apache.  

---

## ✅ Conclusão  

Agora você tem:  
- **MariaDB** rodando dentro do Docker.  
- **phpMyAdmin** acessível em `http://localhost:8080`.  
- **PHP + Apache** acessível em `http://localhost:8000` com suporte a seus arquivos PHP.  
- Dados persistidos no volume `VOL1`.  

Pronto! Seu ambiente de desenvolvimento básico está configurado. 🎉
