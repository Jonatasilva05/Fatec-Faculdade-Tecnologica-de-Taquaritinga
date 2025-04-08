<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="jakarta.tags.core" %>

<jsp:include page="layouttopo.jsp"></jsp:include>

<!-- Seção de introdução -->
<section id="introducao" class="text-center py-5 bg-light">
    <div class="container-fluid">
        <h1 class="display-4 text-dark">Bem-vindo ao Petto!</h1>
        <p class="lead text-muted">Oferecemos os melhores serviços para seu pet. Cuidamos de cada detalhe para garantir o bem-estar do seu amigo.</p>
    </div>
</section>

<!-- Seção de Serviços -->
<section id="servicos" class="py-5" style="background-color: white;">
  <div class="container">
    <h2 class="text-center mb-4">Nossos Serviços</h2>

    <div class="row g-4">

      <!-- Card 1 -->
      <div class="col-md-4">
        <div class="card h-100 border-0 bg-transparent" style="border-radius: 8px;">
          <img src="imagens/i1.jpg" class="card-img-top w-100" height="300" alt="Banho e Tosa" style="border-top-left-radius: 8px; border-top-right-radius: 8px;">
          <div class="card-body" style="background-color: #f0f8ff; border-bottom-left-radius: 8px; border-bottom-right-radius: 8px;">
            <h5 class="card-title">Banho e Tosa</h5>
            <p class="card-text">Cuidamos da higiene do seu pet com muito carinho e atenção.</p>
          </div>
        </div>
      </div>

      <!-- Card 2 -->
      <div class="col-md-4">
        <div class="card h-100 border-0 bg-transparent" style="border-radius: 8px;">
          <img src="imagens/i2.jpg" class="card-img-top w-100" height="300" alt="Adestramento" style="border-top-left-radius: 8px; border-top-right-radius: 8px;">
          <div class="card-body" style="background-color: #f5f5dc; border-bottom-left-radius: 8px; border-bottom-right-radius: 8px;">
            <h5 class="card-title">Adestramento</h5>
            <p class="card-text">Adestramento especializado para o comportamento do seu animal.</p>
          </div>
        </div>
      </div>

      <!-- Card 3 -->
      <div class="col-md-4">
        <div class="card h-100 border-0 bg-transparent" style="border-radius: 8px;">
          <img src="imagens/i3.jpg" class="card-img-top w-100" height="300" alt="Dogwalk" style="border-top-left-radius: 8px; border-top-right-radius: 8px;">
          <div class="card-body" style="background-color: #e6ffe6; border-bottom-left-radius: 8px; border-bottom-right-radius: 8px;">
            <h5 class="card-title">Dogwalk</h5>
            <p class="card-text">Passeios diários para garantir a saúde e bem-estar do seu pet.</p>
          </div>
        </div>
      </div>

    </div>
  </div>
</section>



<!-- Seção de Depoimentos -->
<section id="depoimentos" class="text-center py-5 bg-light">
    <div class="container">
        <h2 class="text-center mb-4">O que nossos clientes dizem</h2>
        <div class="row g-4">
            <!-- Depoimento 1 -->
            <div class="col-md-4">
                <div class="card h-100 border-0 bg-transparent" style="border-radius: 8px;">
                    <div class="card-body" style="background-color: #f0f8ff; border-radius: 8px;">
                        <p class="card-text">"Excelente atendimento! Meu cãozinho adora o banho e tosa. Super recomendo!"</p>
                        <footer class="blockquote-footer">Ana Souza</footer>
                    </div>
                </div>
            </div>

            <!-- Depoimento 2 -->
            <div class="col-md-4">
                <div class="card h-100 border-0 bg-transparent" style="border-radius: 8px;">
                    <div class="card-body" style="background-color: #f5f5dc; border-radius: 8px;">
                        <p class="card-text">"O adestramento foi incrível! Meu cachorro aprendeu muito em pouco tempo."</p>
                        <footer class="blockquote-footer">Carlos Oliveira</footer>
                    </div>
                </div>
            </div>

            <!-- Depoimento 3 -->
            <div class="col-md-4">
                <div class="card h-100 border-0 bg-transparent" style="border-radius: 8px;">
                    <div class="card-body" style="background-color: #e6ffe6; border-radius: 8px;">
                        <p class="card-text">"Os passeios diários ajudam a manter meu pet saudável e feliz. Excelente serviço!"</p>
                        <footer class="blockquote-footer">Mariana Lima</footer>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- Rodapé -->
<jsp:include page="layoutrodape.jsp"></jsp:include>
