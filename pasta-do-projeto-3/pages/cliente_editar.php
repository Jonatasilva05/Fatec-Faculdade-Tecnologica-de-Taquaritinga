<?php

include("../config/database.php");

$id = $_GET['id'];

$result = $conn->query("
SELECT * FROM clientes
WHERE id='$id'
");

$cliente = $result->fetch_assoc();

include("../includes/header.php");
include("../includes/menu.php");

?>

<section class="pricing-section">

<form action="../actions/cliente_update.php" method="POST">

<h2>Editar Cliente</h2>

<p>
Atualize as informações do cliente na plataforma.
</p>

<input
type="hidden"
name="id"
value="<?= $cliente['id'] ?>"
>

<input
type="text"
name="nome"
placeholder="Nome completo"
value="<?= $cliente['nome'] ?>"
required
>

<input
type="email"
name="email"
placeholder="Email"
value="<?= $cliente['email'] ?>"
required
>

<input
type="text"
name="telefone"
placeholder="Telefone"
value="<?= $cliente['telefone'] ?>"
required
>

<button class="btn-primary">
Salvar Alterações
</button>

</form>

</section>

<?php include("../includes/footer.php"); ?>