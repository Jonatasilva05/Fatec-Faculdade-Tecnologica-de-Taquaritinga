<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
  <head>
	<meta charset="UTF-8" />
    <title>SpringMVC</title>
    <link rel="stylesheet" type="text/css" href="css/bootstrap5/css/bootstrap.css" />
    <link rel="stylesheet" type="text/css" href="css/estilos.css" />
    <link rel="stylesheet" type="text/css" href="css/cadastrarlivro.css">

    <script src="js/jquery-3.2.1.slim.min.js"></script>
    <script src="js/script.js"></script>
    <script src="css/bootstrap5/js/bootstrap.min.js"></script>
  </head>
    <header>
      <nav class="navbar navbar-expand-lg bg-dark">
        <div class="container-fluid">
          <a class="navbar-brand text-white" href="#">Petto</a>
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Alternar navegação">
            <span class="navbar-toggler-icon"></span>
          </button>
    
          <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav ms-auto">
              <li class="nav-item">
                <a class="nav-link" href="index.html"><i class="fas fa-home"></i> 
                  <span class="text-pt">Início</span>
                  <span class="text-en hidden">Home</span>
                  <span class="text-es hidden">Inicio</span>
                </a>
              </li>
              
              <li class="nav-item">
                <a class="nav-link" href="painel.php"><i class="fas fa-syringe"></i> 
                  <span class="text-pt">Vacinação</span>
                  <span class="text-en hidden">Vaccination</span>
                  <span class="text-es hidden">Vacunación</span>
                </a>
              </li>
    
              <li class="nav-item">
                <a class="nav-link" href="Pagina5.html"><i class="fas fa-phone"></i> 
                  <span class="text-pt">Contato</span>
                  <span class="text-en hidden">Contact</span>
                  <span class="text-es hidden">Contacto</span>              
                </a>
              </li>
    
              <li class="nav-item">
                <a class="nav-link" href="index.php"><i class="fas fa-sign-in-alt"></i> 
                  <span class="text-pt">Entrar</span>
                  <span class="text-en hidden">Login</span>
                  <span class="text-es hidden">Iniciar sesión</span>
                </a>
              </li>
    
              <li class="nav-item">
                <a class="nav-link" href="register.php"><i class="fas fa-user-plus"></i> 
                  <span class="text-pt">Cadastrar-se</span>
                  <span class="text-en hidden">Sign Up</span>
                  <span class="text-es hidden">Registrarse</span>
                </a>
              </li>
    
              <li class="nav-item dropdown">
                <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                  <span class="text-pt">Acessibilidade</span>
                  <span class="text-en hidden">Accessibility</span>
                  <span class="text-es hidden">Accesibilidad</span>
                </a>
                <ul class="dropdown-menu" id="acessibilidadeMenu">
                  <li>
                    <a class="dropdown-item" href="#" onclick="alterarTamanhoTexto(1.1); event.stopPropagation();">A+</a>
                  </li>
    
                  <li>
                    <a class="dropdown-item" href="#" onclick="alterarTamanhoTexto(0.9); event.stopPropagation();">A-</a>
                  </li>
    
                  <li>
                    <hr class="dropdown-divider">
                  </li>
    
                  <li>
                    <a class="dropdown-item" href="#">
                      <span class="text-pt">
                        <button id="toggle-dark-mode modoEscuro">Modo Escuro</button>
                      </span>
                      <span class="text-en hidden">
                        <button id="modoDark">Dark Mode</button>
                      </span>
                      <span class="text-es hidden">
                        <button id="modoOscuro">Modo oscuro</button>
                      </span>
                    </a>
                  </li>
                </ul>
              </li>
            </ul>
    
            <!-- Botão da Bandeira(flag) dos Estados Unidos (idioma Inglês-Americano)-->
            <button class="btn btn-outline-light ms-3" id="toggleEn">
              <img src="imagens/flagEUA.jpg" id="flagEn" alt="Bandeira dos EUA">
            </button>
          
            <!-- Botão da Bandeira(flag) da Espanha (idioma Espanhol) -->
            <button class="btn btn-outline-light ms-3" id="toggleEs">
              <img src="imagens/flagEspanha.jpg" id="flagEs" alt="Bandeira da Espanha">
            </button>
          
            <!-- Botão da Bandeira(flag) do Brasil (idioma Português-Brasil) -->
            <button class="btn btn-outline-light ms-3" id="togglePt" style="display: none;">
              <img src="imagens/flagBrasil.jpg" id="flagPt" alt="Bandeira do Brasil">
            </button>
    
          </div>
        </div>
      </nav>	  
    </header>
        <body>
    <main>
      <div class="container">
