USE meubanco;

-- Tabela de clientes/usuários do sistema (O CRUD que você já tem)
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL
);

-- NOVA TABELA: Apenas para quem faz LOGIN
CREATE TABLE IF NOT EXISTS admins (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
);

-- Criar o login inicial padrão
INSERT INTO admins (email, password) VALUES ('admin@admin.com', '123456');