<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="jakarta.tags.core" %>
<jsp:include page="layouttopo.jsp" />

<main style="font-family: 'Segoe UI', 'Roboto', 'Helvetica Neue', sans-serif;">

  <!-- Seção de Introdução -->
  <section class="py-5 bg-light text-center">
    <div class="container">
      <h1 class="display-4 text-dark fw-semibold">Carteira de Vacinação</h1>
      <p class="lead fs-5 text-muted">
        A carteira de vacinação é essencial para garantir a saúde e bem-estar do seu pet. Ela registra todas as vacinas aplicadas, funcionando como um histórico vital para os cuidados do seu companheiro.
      </p>
    </div>
  </section>

  <!-- Seção O que é -->
  <section id="o-que-e" class="py-5">
    <div class="container">
      <div class="row align-items-center g-5">
        <div class="col-md-6">
          <h2 class="fs-2 fw-semibold mb-4">O que é a Carteira de Vacinação?</h2>
          <p class="fs-5 text-muted">
            A carteira de vacinação é um documento oficial que registra todas as vacinas administradas ao seu pet. Essencial para comprovar que ele está protegido contra doenças graves, ela permite acompanhar o histórico vacinal de forma segura e prática.
          </p>
          <p class="fs-5 text-muted">
            Com a carteira em mãos, tutores e veterinários podem tomar decisões baseadas em dados confiáveis, garantindo mais saúde e longevidade para os animais.
          </p>
        </div>
        <div class="col-md-6">
          <img src="imagens/i7.jpg" alt="Imagem da Carteira de Vacinação" class="img-fluid rounded-4 shadow" style="max-height: 400px; object-fit: cover; width: 100%;">
        </div>
      </div>
    </div>
  </section>

  <!-- Seção Como Atualizar -->
  <section id="como-atualizar" class="py-5 bg-light">
    <div class="container">
      <div class="row align-items-center g-5">
        <div class="col-md-6">
          <img src="imagens/i5.jpg" alt="Veterinário atualizando vacinação" class="img-fluid rounded-4 shadow" style="max-height: 400px; object-fit: cover; width: 100%;">
        </div>
        <div class="col-md-6">
          <h2 class="fs-2 fw-semibold mb-4">Como Atualizar a Carteira?</h2>
          <p class="fs-5 text-muted">
            A carteira deve ser atualizada conforme o cronograma de vacinação do seu pet. O veterinário registra cada vacina aplicada, incluindo data, lote e validade.
          </p>
          <ul class="fs-5 text-muted">
            <li>Visite o veterinário regularmente.</li>
            <li>Fique atento às datas de reforço das vacinas.</li>
            <li>Armazene a carteira em um local seguro e acessível.</li>
          </ul>
        </div>
      </div>
    </div>
  </section>

  <!-- Seção Conclusão -->
  <section id="conclusao" class="py-5">
    <div class="container text-center">
      <h2 class="fs-2 fw-semibold mb-4">Manter a Carteira de Vacinação em Dia é Essencial!</h2>
      <p class="fs-5 text-muted">
        A vacinação é um gesto de amor e responsabilidade. Atualizar a carteira garante o bem-estar do seu pet e contribui para uma vida longa e saudável ao seu lado.
      </p>
    </div>
  </section>

</main>

<jsp:include page="layoutrodape.jsp" />
