<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="jakarta.tags.core" %>
<jsp:include page="layouttopo.jsp" />

<main style="font-family: 'Segoe UI', 'Roboto', 'Helvetica Neue', sans-serif;">

  <!-- Seção Introdução -->
  <section class="py-5 bg-light text-center">
    <div class="container">
      <h1 class="display-4 text-dark">Nossos Serviços</h1>
      <p class="lead fs-5 text-muted">
        Soluções pensadas para garantir saúde, bem-estar e praticidade no cuidado com seu pet.
      </p>
    </div>
  </section>

  <!-- Serviço 1: Lembrete -->
  <section class="py-5">
    <div class="container">
      <div class="row align-items-center">
        <div class="col-md-6">
          <img src="imagens/i8.jpg" alt="Lembrete de Vacinas" class="img-fluid rounded-4 shadow">
        </div>
        <div class="col-md-6">
          <h2 class="fs-2 fw-semibold mb-4">Lembrete de Vacinação</h2>
          <p class="fs-5 text-muted">
            Nunca mais perca o prazo de uma vacina! Com nosso sistema inteligente, você recebe alertas automáticos quando a vacinação do seu pet estiver próxima de vencer.
          </p>
          <p class="fs-5 text-muted">
            Mais tranquilidade e responsabilidade para manter a saúde do seu melhor amigo em dia.
          </p>
        </div>
      </div>
    </div>
  </section>

  <!-- Serviço 2: Carteira Digital -->
  <section class="py-5 bg-light">
    <div class="container">
      <div class="row align-items-center">
        <div class="col-md-6 order-md-2">
          <img src="imagens/i9.jpg" alt="Carteira Digital" class="img-fluid rounded-4 shadow">
        </div>
        <div class="col-md-6 order-md-1">
          <h2 class="fs-2 fw-semibold mb-4">Carteira de Vacinação Digital</h2>
          <p class="fs-5 text-muted">
            Organize todas as informações de saúde do seu pet em um só lugar. A carteira digital registra vacinas, datas, doses e muito mais, disponível a qualquer momento.
          </p>
          <p class="fs-5 text-muted">
            Ideal para apresentar em consultas ou emergências veterinárias.
          </p>
        </div>
      </div>
    </div>
  </section>

  <!-- Serviço 3: Dogwalk -->
  <section class="py-5">
    <div class="container">
      <div class="row align-items-center">
        <div class="col-md-6">
          <img src="imagens/i10.jpg" alt="Dogwalk - Passeios com Pets" class="img-fluid rounded-4 shadow">
        </div>
        <div class="col-md-6">
          <h2 class="fs-2 fw-semibold mb-4">Dogwalk</h2>
          <p class="fs-5 text-muted">
            Passeios seguros, monitorados e cheios de diversão para o seu pet gastar energia e manter a saúde em dia.
          </p>
          <p class="fs-5 text-muted">
            Nossa equipe é treinada para lidar com diferentes raças e temperamentos, sempre com foco no conforto e bem-estar do animal.
          </p>
        </div>
      </div>
    </div>
  </section>

</main>

<jsp:include page="layoutrodape.jsp" />
