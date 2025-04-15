<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="jakarta.tags.core" %>
<jsp:include page="layouttopo.jsp" />

<main style="font-family: 'Segoe UI', 'Roboto', 'Helvetica Neue', sans-serif;">

  <!-- Seção Introdução -->
  <section class="py-5 bg-light text-center">
    <div class="container">
      <h1 class="display-4 text-dark fw-semibold">Sobre a Petto</h1>
      <p class="lead fs-5 text-muted">
        Uma história de amor, cuidado e dedicação aos nossos melhores amigos de quatro patas.
      </p>
    </div>
  </section>

  <!-- Seção Nossa História -->
  <section class="py-5">
    <div class="container">
      <div class="row align-items-center">
        <div class="col-md-6">
          <h2 class="fs-2 fw-semibold mb-4">Nossa História</h2>
          <p class="fs-5 text-muted">
            Fundada com o propósito de transformar a vida dos pets e seus tutores, a <strong>Petto</strong> surgiu da paixão por animais e do desejo de oferecer um espaço onde o cuidado, a segurança e o carinho fossem prioridade.
          </p>
          <p class="fs-5 text-muted">
            Desde os primeiros atendimentos, nossa missão sempre foi proporcionar uma experiência completa — do banho e tosa até serviços como adestramento, passeios e vacinação.
          </p>
        </div>
        <div class="col-md-6">
          <img src="imagens/i4.jpg" alt="Pet sendo cuidado com carinho" class="img-fluid rounded-4 shadow">
        </div>
      </div>
    </div>
  </section>

  <!-- Seção Diferenciais (agora no meio) -->
  <section class="py-5 bg-light text-center">
    <div class="container">
      <h2 class="fs-2 fw-semibold mb-5">Por que escolher a Petto?</h2>
      <div class="row g-4">
        <div class="col-md-4">
          <div class="card h-100 border-0 bg-transparent">
            <div class="card-body" style="background-color: #f0f8ff; border-radius: 8px;">
              <h5 class="card-title fs-4 fw-semibold">Equipe Especializada</h5>
              <p class="card-text fs-5 text-muted">Profissionais capacitados, treinados para garantir o melhor atendimento ao seu pet.</p>
            </div>
          </div>
        </div>
        <div class="col-md-4">
          <div class="card h-100 border-0 bg-transparent">
            <div class="card-body" style="background-color: #f0f8ff; border-radius: 8px;">
              <h5 class="card-title fs-4 fw-semibold">Ambiente Seguro</h5>
              <p class="card-text fs-5 text-muted">Espaços planejados para segurança, conforto e tranquilidade dos animais.</p>
            </div>
          </div>
        </div>
        <div class="col-md-4">
          <div class="card h-100 border-0 bg-transparent">
            <div class="card-body" style="background-color: #f0f8ff; border-radius: 8px;">
              <h5 class="card-title fs-4 fw-semibold">Atendimento Humanizado</h5>
              <p class="card-text fs-5 text-muted">Relacionamento próximo, escutando cada tutor com atenção e carinho.</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Seção Missão, Visão e Valores -->
  <section class="py-5">
    <div class="container">
      <div class="row align-items-center">
        <div class="col-md-6 order-md-2">
          <h2 class="fs-2 fw-semibold mb-4">Missão, Visão e Valores</h2>
          <ul class="fs-5 text-muted">
            <li><strong>Missão:</strong> Cuidar da saúde, bem-estar e felicidade dos pets com excelência e responsabilidade.</li>
            <li><strong>Visão:</strong> Ser referência em atendimento e serviços especializados no cuidado com os animais.</li>
            <li><strong>Valores:</strong> Amor pelos animais, ética profissional, respeito aos clientes e compromisso com a qualidade.</li>
          </ul>
        </div>
        <div class="col-md-6 order-md-1">
          <img src="imagens/i5.jpg" alt="Profissionais da Petto com cães" class="img-fluid rounded-4 shadow">
        </div>
      </div>
    </div>
  </section>

</main>

<jsp:include page="layoutrodape.jsp" />
