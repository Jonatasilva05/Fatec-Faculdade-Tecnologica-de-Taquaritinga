<?php
session_start();
require_once 'config.php';

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $nome = $_POST['nome'];
    $email = $_POST['email'];
    $username = $_POST['username'];
    $senha = $_POST['password'];
    $hashed_password = password_hash($senha, PASSWORD_BCRYPT);

    $sql = "SELECT * FROM users WHERE email = ? OR username = ?";
    $stmt = $conn->prepare($sql);
    $stmt->bind_param("ss", $email, $username);
    $stmt->execute();
    $result = $stmt->get_result();

    if ($result->num_rows > 0) {
        echo "E-mail ou nome de usuário já estão em uso! <br> tente novamente";
    } else {
        
        $sql = "INSERT INTO users (nome, email, username, senha) VALUES (?, ?, ?, ?)";
        $stmt = $conn->prepare($sql);
        $stmt->bind_param("ssss", $nome, $email, $username, $hashed_password);

        if ($stmt->execute()) {
            $_SESSION['message'] = "Cadastro realizado com sucesso!";
            header("Location: ../Tela-login/index.html");
            exit();
        } else {
            echo "Erro ao cadastrar: " . $stmt->error;
        }
    }

    $stmt->close();
    $conn->close();
}
?>