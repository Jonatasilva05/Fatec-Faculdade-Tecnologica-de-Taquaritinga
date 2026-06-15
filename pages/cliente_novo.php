<?php
include("../includes/header.php");
include("../includes/menu.php");


?>

<section class="pricing-section">

<form action="../actions/cliente_create.php" method="POST">

<h2>Novo Cliente</h2>

<p>
Cadastre um novo cliente na plataforma NovaPay.
</p>

<input type="text" name="nome" placeholder="Nome completo">

<input type="email" name="email" placeholder="Email">

<input type="text" name="telefone" placeholder="Telefone">

<button class="btn-primary">
Cadastrar Cliente
</button>

</form>

</section>

<?php include("../includes/footer.php"); ?>