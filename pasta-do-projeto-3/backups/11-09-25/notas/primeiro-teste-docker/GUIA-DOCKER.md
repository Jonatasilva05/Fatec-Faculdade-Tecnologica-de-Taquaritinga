# 🚀 Guia Rápido: Docker com MariaDB, PHP e phpMyAdmin  

Este guia ensina, de forma simples e prática, como configurar um ambiente básico com **MariaDB**, **PHP** e **phpMyAdmin** usando Docker.  

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

Exemplo de saída:  

```
NETWORK ID     NAME      DRIVER    SCOPE
261ce2acb328   REDE1     bridge    local
346aaaecbeb6   bridge    bridge    local
decd9b9b9b41   host      host      local
b8db33d18e97   none      null      local
```

---

## 2. Criando o Volume para os Dados  

Agora vamos criar um volume para persistir os dados do banco de dados:  

```bash
docker volume create VOL1
```

Para confirmar:  

```bash
docker volume ls
```

Saída esperada:  

```
DRIVER    VOLUME NAME
local     VOL1
```

> 🔑 **Dica:** use sempre nomes simples (somente letras e números, sem caracteres especiais).  

---

## 3. Subindo o Container do MariaDB  

Baixe e execute o **MariaDB** (um substituto 100% compatível com MySQL):  

```bash
docker run -d --name MARIADB -v VOL1:/var/lib/mysql -h db   --network REDE1 --env MARIADB_USER=user --env MARIADB_PASSWORD=senha12345 --env MARIADB_ROOT_PASSWORD=senharoot123 mariadb:latest
```

Ou execute com quebra de linha

```bash
docker run -d \
--name MARIADB \
-v VOL1:/var/lib/mysql \
-h db \
--network REDE1 \
--env MARIADB_USER=user \
--env MARIADB_PASSWORD=senha12345 \
--env MARIADB_ROOT_PASSWORD=senharoot123 \
mariadb:latest
```


### O que cada parâmetro significa:
- `docker run` → cria e executa um container.  
- `-d` → executa em segundo plano.  
- `--name MARIADB` → nome do container.  
- `-v VOL1:/var/lib/mysql` → mapeia o volume `VOL1` para os dados do banco.  
- `-h db` → define o hostname do container (será usado para conectar ao phpMyAdmin).  
- `--network REDE1` → conecta à rede que criamos.  
- `--env MARIADB_USER=user` → cria um usuário comum.  
- `--env MARIADB_PASSWORD=senha12345` → senha do usuário comum.  
- `--env MARIADB_ROOT_PASSWORD=senharoot123` → senha do administrador (root).  
- `mariadb:latest` → usa a versão mais recente da imagem oficial do MariaDB.  

Para inspecionar e confirmar a configuração:  

```bash
docker inspect MARIADB
```

---

## 4. Subindo o Container do phpMyAdmin  

Agora vamos configurar o **phpMyAdmin** para gerenciar o banco via navegador:  

```bash
docker run -d --name MYADMIN -h myadmin --network REDE1 -e PMA_HOST=db -p 8080:80 phpmyadmin:latest
```

Ou execute com quebra de linha

```bash
docker run -d \
--name MYADMIN \
-h myadmin \
--network REDE1 \
-e PMA_HOST=db \
-p 8080:80 \
phpmyadmin:latest
```

### Explicação:
- `--name MYADMIN` → nome do container phpMyAdmin.  
- `-h myadmin` → hostname do phpMyAdmin.  
- `--network REDE1` → conecta à mesma rede do MariaDB.  
- `-e PMA_HOST=db` → indica onde está o banco (hostname `db` definido no container do MariaDB).  
- `-p 8080:80` → expõe a porta 8080 do host para acessar o phpMyAdmin no navegador.  
- `phpmyadmin:latest` → imagem oficial mais atualizada.  

---

## 5. Acessando o phpMyAdmin  

Abra no navegador:  

```
http://localhost:8080
```

- **Servidor (host):** `db`  
- **Usuário:** `user` (ou `root`)  
- **Senha:** `senha12345` (ou `senharoot123` para root)  

---

## 6. Backup do Volume  

Se quiser fazer backup do volume manualmente, no **Windows** vá até:  

```
C:\Users\<SEU_USUARIO>\AppData\Local\Docker\wsl\data
```

No **Linux**, os volumes ficam em:  

```
/var/lib/docker/volumes
```

---

## ✅ Conclusão  

Pronto! Agora você tem:  
- Um **MariaDB** rodando dentro do Docker.  
- Um **phpMyAdmin** acessível via navegador em `http://localhost:8080`.  
- Dados persistidos em um volume (`VOL1`).  

---

👉 Esse setup é ótimo para **testes rápidos e projetos básicos**.  
Se precisar evoluir, pode migrar facilmente para **Docker Compose** e automatizar tudo com um único arquivo.  