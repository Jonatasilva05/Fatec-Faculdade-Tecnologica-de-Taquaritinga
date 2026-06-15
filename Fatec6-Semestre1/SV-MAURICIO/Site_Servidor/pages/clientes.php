<?php
include("../config/database.php");
include("../includes/header.php");
include("../includes/menu.php");

$clientes = $conn->query("
SELECT * FROM clientes
ORDER BY id DESC
");
?>

<section class="features-section">

<div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:20px;">

<h2 class="section-title">
Clientes
</h2>

<a href="cliente_novo.php" class="btn-primary">
Novo Cliente
</a>

</div>

<table style="width:100%;">

<tr>
<th>Nome</th>
<th>Email</th>
<th>Telefone</th>
<th>Ações</th>
</tr>

<?php while($cliente = $clientes->fetch_assoc()): ?>

<tr>

<td><?= $cliente['nome'] ?></td>

<td><?= $cliente['email'] ?></td>

<td><?= $cliente['telefone'] ?></td>

<td>

<a href="cliente_editar.php?id=<?= $cliente['id'] ?>">
Editar
</a>

|

<a href="../actions/cliente_delete.php?id=<?= $cliente['id'] ?>">
Excluir
</a>

</td>

</tr>

<?php endwhile; ?>

</table>

</section>

<?php include("../includes/footer.php"); ?>