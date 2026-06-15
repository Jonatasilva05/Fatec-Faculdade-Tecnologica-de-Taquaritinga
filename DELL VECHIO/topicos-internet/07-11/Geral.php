<?php

    class Geral{

        public function media(int $nota1, int $nota2): int{
            $mediaFinal = $nota1 + $nota2;
            $mediaFinal2 = $mediaFinal / 2;
            return $mediaFinal2;
        }

    }

?>