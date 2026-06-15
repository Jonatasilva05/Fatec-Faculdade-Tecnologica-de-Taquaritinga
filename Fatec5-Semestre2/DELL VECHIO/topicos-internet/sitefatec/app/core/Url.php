<?php

    class Url{

        public string $url;

        public function refinarUrl(string $urlcrua) {

            // GERA UM ARRAY QUE DIVIDE A STRING EM DUAS PARTES
            $partes = parse_url($urlcrua); 

            // COLETA APENAS A PARTE DA URL, SEM AS QUERIES
            $caminho = $partes["path"];

            // REFINA RETIRANDO BARRA DO INICIO E FIM DO STRING
            $caminho = trim($caminho, "/");

            // EXPLODE O STRING EM ARRAY COM BASE NAS BARRAS RESTANTES
            $arraycaminho = explode("/", $caminho);

            // VERSÃO FINAL E REFINADA
            $urlrefinada = $arraycaminho[0];

            $this->url = $urlrefinada;
            return $urlrefinada;
        }

    }

?>