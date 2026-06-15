<?php

    include_once  __DIR__ . "/app/core/Url.php";

    $objUrl = new Url();

    $urlcrua = $_SERVER["REQUEST_URI"];

    $urlrefinada = $objUrl->refinarUrl($urlcrua);

    echo $url;

?>