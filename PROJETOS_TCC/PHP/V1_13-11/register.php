<?php
session_start();
require_once 'config.php';

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $nome = $_POST['nome'];
    $email = $_POST['email'];
    $username = $_POST['username'];
    $senha = $_POST['password'];
    $hashed_password = password_hash($senha, PASSWORD_BCRYPT);

    // Verificar se o e-mail ou o nome de usuário já estão em uso
    $sql = "SELECT * FROM users WHERE email = ? OR username = ?";
    $stmt = $conn->prepare($sql);
    $stmt->bind_param("ss", $email, $username);
    $stmt->execute();
    $result = $stmt->get_result();

    if ($result->num_rows > 0) {
        echo "E-mail ou nome de usuário já estão em uso! <br> tente novamente";
    } else {
        // Inserir novo usuário
        $sql = "INSERT INTO users (nome, email, username, senha) VALUES (?, ?, ?, ?)";
        $stmt = $conn->prepare($sql);
        $stmt->bind_param("ssss", $nome, $email, $username, $hashed_password);

        if ($stmt->execute()) {
            $_SESSION['message'] = "Cadastro realizado com sucesso!";
            header("Location: login.php");
            exit();
        } else {
            echo "Erro ao cadastrar: " . $stmt->error;
        }
    }

    $stmt->close();
    $conn->close();
}
?>

<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Criar Conta</title>
</head>
<body>
    <h1>Criar Conta</h1>
    <form method="POST" action="register.php">
        <input type="text" name="nome" placeholder="Nome" required>
        <input type="email" name="email" placeholder="Email" required>
        <input type="text" name="username" placeholder="Nome de Usuário" required>
        <input type="password" name="password" placeholder="Senha" required>
        <button type="submit">Cadastrar</button>
    </form>
    <p>Já tem conta? <a href="login.php">Login</a></p>
</body>
</html>
