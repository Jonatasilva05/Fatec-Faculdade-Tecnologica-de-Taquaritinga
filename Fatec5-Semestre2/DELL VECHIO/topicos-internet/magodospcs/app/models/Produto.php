<?php

    class Produto{

        private int $id;
        private string $nome;
        private string $descricao;
        private int $preco;
        private string $categoria;
        private string $marca;
        private string $cor;
        private int $largura;
        private int $altura;
        private int $profundidade;
        private int $ativo;

        public function __construct(){
            
            $this->id = 0;
            $this->nome = "";
            $this->descricao = "";
            $this->preco = 0;
            $this->categoria = "";
            $this->marca = "";
            $this->cor = "";
            $this->largura = 0;
            $this->altura = 0;
            $this->profundidade = 0;
            $this->ativo = 1;

        }

        // GET ou GETTERS é o "padrao" entre os desenvolvedores para puxar, obter, consultar
        public function getId(){
            return $this->id;
        }

        // SET ou SETTERS é o "padrao" entre os desenvolvedores para gravar, escrever
        public function setId(int $valor){
            $this->id = $valor;
        }

        public function getNome(){
            return $this->nome;
        }

        public function setNome(string $nome){
            $this->nome = $nome;
        }
        
        public function getMarca(){
            return $this->marca;
        }

        public function setMarca(string $marca){
            $this->marca = $marca;
        }

    };

?>