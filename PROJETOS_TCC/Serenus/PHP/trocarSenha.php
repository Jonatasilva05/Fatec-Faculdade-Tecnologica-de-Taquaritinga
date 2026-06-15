<?php
session_start();
require_once 'config.php';

if (!isset($_SESSION['user_id'])) {
    header("Location: ./login.php");
    exit();
}

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    if (isset($_POST['nova_senha']) && isset($_POST['confirma_senha'])) {
        $senha_nova = $_POST['nova_senha'];
        $senha_confirmacao = $_POST['confirma_senha'];

        // vai verificar se as senhas estao iguais
        if ($senha_nova !== $senha_confirmacao) {
            echo "As senhas novas não coincidem.";
        } else {
            
            $senha_nova_hash = password_hash($senha_nova, PASSWORD_DEFAULT);

            // vai autalizar a nova senha no banco
            $user_id = $_SESSION['user_id'];
            $sql_update = "UPDATE users SET senha = ? WHERE id = ?";
            $stmt_update = $conn->prepare($sql_update);
            $stmt_update->bind_param("si", $senha_nova_hash, $user_id);

            if ($stmt_update->execute()) {
                echo "Senha alterada com sucesso.";
            } else {
                echo "Erro ao atualizar a senha.";
            }

            $stmt_update->close();
        }
    } else {
        echo "Por favor, preencha todos os campos do formulário.";
    }
    $conn->close();
}
?>

<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Alterar Senha</title>
</head>
<body>
    <h2>Alterar Senha</h2>
    <form method="POST" action="">
        <label for="nova_senha">Nova Senha:</label>
        <input type="password" name="nova_senha" required><br><br>

        <label for="confirma_senha">Confirmar Nova Senha:</label>
        <input type="password" name="confirma_senha" required><br><br>

        <button type="submit">Alterar Senha</button>
    </form>
</body>
</html>
