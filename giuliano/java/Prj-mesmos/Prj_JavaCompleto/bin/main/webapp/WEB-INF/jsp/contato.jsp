<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="jakarta.tags.core" %>
<jsp:include page="layouttopo.jsp" />

<main style="font-family: 'Segoe UI', 'Roboto', 'Helvetica Neue', sans-serif;">

  <!-- Seção Contato - Cabeçalho -->
  <section class="py-5 bg-light text-center">
    <div class="container">
      <h1 class="display-5 fw-semibold text-dark">Fale Conosco</h1>
      <p class="lead fs-5 text-muted">
        Entre em contato conosco para tirar dúvidas, agendar um serviço ou deixar sua sugestão.
      </p>
    </div>
  </section>

  <!-- Seção Contato - Formulário -->
  <section class="py-5">
    <div class="container">
      <div class="row justify-content-center">
        <div class="col-md-8">
          <form action="enviarContato.jsp" method="post" class="p-4 shadow rounded-4 bg-light">
            <div class="mb-3">
              <label for="nome" class="form-label">Nome</label>
              <input type="text" class="form-control" id="nome" name="nome" required>
            </div>
            <div class="mb-3">
              <label for="email" class="form-label">E-mail</label>
              <input type="email" class="form-control" id="email" name="email" required>
            </div>
            <div class="mb-3">
              <label for="assunto" class="form-label">Assunto</label>
              <input type="text" class="form-control" id="assunto" name="assunto">
            </div>
            <div class="mb-3">
              <label for="mensagem" class="form-label">Mensagem</label>
              <textarea class="form-control" id="mensagem" name="mensagem" rows="5" required></textarea>
            </div>
            <button type="submit" class="btn btn-primary px-4">Enviar</button>
          </form>
        </div>
      </div>
    </div>
  </section>

  <!-- Seção Informações de Contato -->
  <section class="py-5 bg-light text-center">
    <div class="container">
      <h2 class="fs-3 fw-semibold mb-4">Informações de Contato</h2>
      <p class="fs-5 text-muted">Estamos localizados em:</p>
      <p class="fs-5 text-muted mb-2"><i class="bi bi-geo-alt-fill"></i> Rua dos Pets, 123 - Petlândia, SP</p>
      <p class="fs-5 text-muted mb-2"><i class="bi bi-envelope-fill"></i> contato@petto.com.br</p>
      <p class="fs-5 text-muted"><i class="bi bi-telephone-fill"></i> (11) 99999-9999</p>
    </div>
  </section>

</main>

<jsp:include page="layoutrodape.jsp" />
