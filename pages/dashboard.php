<?php
include("../config/database.php");
include("../includes/header.php");
include("../includes/menu.php");

$totalClientes = $conn->query("
SELECT COUNT(*) as total FROM clientes
")->fetch_assoc()['total'];

$totalEntradas = $conn->query("
SELECT SUM(valor) as total
FROM transacoes 
WHERE tipo='entrada'
")->fetch_assoc()['total'];

$totalSaidas = $conn->query("
SELECT SUM(valor) as total
FROM transacoes
WHERE tipo='saida'
")->fetch_assoc()['total'];
?>

<section class="stats-section">

<div class="stat-block">

<div class="stat-num">
<?= $totalClientes ?>
</div>

<div class="stat-label">
Clientes
</div>

</div>

<div class="stat-block">

<div class="stat-num">
R$ <?= number_format($totalEntradas,2,',','.') ?>
</div>

<div class="stat-label">
Entradas
</div>

</div>

<div class="stat-block">

<div class="stat-num">
R$ <?= number_format($totalSaidas,2,',','.') ?>
</div>

<div class="stat-label">
Saídas
</div>

</div>

</section>

<?php include("../includes/footer.php"); ?>