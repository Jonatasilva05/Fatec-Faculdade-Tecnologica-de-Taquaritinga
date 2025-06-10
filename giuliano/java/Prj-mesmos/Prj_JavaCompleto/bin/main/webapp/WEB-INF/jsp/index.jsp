<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="jakarta.tags.core" %>
<jsp:include page="layouttopo.jsp" />

<main style="font-family: 'Segoe UI', 'Roboto', 'Helvetica Neue', sans-serif;">

  <!-- Seção Introdução -->
  <section class="py-5 bg-light text-center">
    <div class="container">
      <h1 class="display-4 text-dark fw-semibold">Bem-vindo ao Petto!</h1>
      <p class="lead fs-5 text-muted">
        Oferecemos os melhores serviços para o seu pet. Cuidamos de cada detalhe para garantir o bem-estar do seu amigo.
      </p>
    </div>
  </section>

<!-- Seção Quem Somos -->
<section class="py-5 text-center">
  <div class="container">
    <h2 class="fs-2 fw-semibold mb-4">Quem Somos</h2>
    <div class="row align-items-center">
      <div class="col-md-6">
        <p class="fs-5 text-muted mb-4">
          A <strong>Petto</strong> nasceu com o propósito de oferecer serviços de alta qualidade para o bem-estar dos animais. Somos apaixonados por pets e comprometidos em proporcionar o melhor cuidado e atenção a cada um deles.
        </p>
        <p class="fs-5 text-muted mb-4">
          Com uma equipe especializada e apaixonada, temos como missão transformar a vida dos seus pets, oferecendo serviços personalizados que atendem às suas necessidades específicas, como banho e tosa, adestramento, dogwalk e muito mais.
        </p>
        <p class="fs-5 text-muted mb-4">
          Nosso compromisso é com a qualidade, segurança e carinho, garantindo que seu pet receba o melhor atendimento possível. Porque para nós, o seu pet é como da família.
        </p>
      </div>
      <div class="col-md-6">
        <img src="imagens/i6.jpg" alt="Equipe Petto com pets" class="img-fluid rounded-4 shadow">
      </div>
    </div>
  </div>
</section>

  <!-- Seção Serviços -->
  <section class="py-5">
    <div class="container">
      <h2 class="fs-2 fw-semibold mb-4 text-center">Nossos Serviços</h2>
      <div class="row g-4 text-center">
        <div class="col-md-4">
          <div class="card h-100 border-0 bg-transparent" style="border-radius: 8px;">
            <img src="imagens/i1.jpg" class="card-img-top w-100" height="300" alt="Banho e Tosa" style="border-top-left-radius: 8px; border-top-right-radius: 8px;">
            <div class="card-body" style="background-color: #f0f8ff; border-bottom-left-radius: 8px; border-bottom-right-radius: 8px;">
              <h5 class="card-title fs-4 fw-semibold">Lembrete</h5>
              <p class="card-text fs-5 text-muted">O Lembrete avisa quando está perto de vencer uma vacina.</p>
            </div>
          </div>
        </div>

        <div class="col-md-4">
          <div class="card h-100 border-0 bg-transparent" style="border-radius: 8px;">
            <img src="imagens/i2.jpg" class="card-img-top w-100" height="300" alt="Adestramento" style="border-top-left-radius: 8px; border-top-right-radius: 8px;">
            <div class="card-body" style="background-color: #f0f8ff; border-bottom-left-radius: 8px; border-bottom-right-radius: 8px;">
              <h5 class="card-title fs-4 fw-semibold">Vacinação</h5>
              <p class="card-text fs-5 text-muted">A carteira digital de Vacinação deixa em dia as informações do seu animal.</p>
            </div>
          </div>
        </div>

        <div class="col-md-4">
          <div class="card h-100 border-0 bg-transparent" style="border-radius: 8px;">
            <img src="imagens/i3.jpg" class="card-img-top w-100" height="300" alt="Dogwalk" style="border-top-left-radius: 8px; border-top-right-radius: 8px;">
            <div class="card-body" style="background-color: #f0f8ff; border-bottom-left-radius: 8px; border-bottom-right-radius: 8px;">
              <h5 class="card-title fs-4 fw-semibold">Dogwalk</h5>
              <p class="card-text fs-5 text-muted">Passeios diários para garantir a saúde e bem-estar do seu pet.</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Seção Depoimentos -->
  <section class="py-5 bg-light text-center">
    <div class="container">
      <h2 class="fs-2 fw-semibold mb-4">O que nossos clientes dizem</h2>
      <div class="row g-4">
        <div class="col-md-4">
          <div class="card h-100 border-0 bg-transparent" style="border-radius: 8px;">
            <div class="card-body" style="background-color: #f0f8ff; border-radius: 8px;">
              <p class="card-text fs-5 fst-italic">"Excelente atendimento! Meu cãozinho adora o banho e tosa. Super recomendo!"</p>
              <footer class="blockquote-footer fs-5 mt-3">Ana Souza</footer>
            </div>
          </div>
        </div>

        <div class="col-md-4">
          <div class="card h-100 border-0 bg-transparent" style="border-radius: 8px;">
            <div class="card-body" style="background-color: #f0f8ff; border-radius: 8px;">
              <p class="card-text fs-5 fst-italic">"O adestramento foi incrível! Meu cachorro aprendeu muito em pouco tempo."</p>
              <footer class="blockquote-footer fs-5 mt-3">Carlos Oliveira</footer>
            </div>
          </div>
        </div>

        <div class="col-md-4">
          <div class="card h-100 border-0 bg-transparent" style="border-radius: 8px;">
            <div class="card-body" style="background-color: #f0f8ff; border-radius: 8px;">
              <p class="card-text fs-5 fst-italic">"Os passeios diários ajudam a manter meu pet saudável e feliz. Excelente serviço!"</p>
              <footer class="blockquote-footer fs-5 mt-3">Mariana Lima</footer>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  
</main>

<jsp:include page="layoutrodape.jsp" />
