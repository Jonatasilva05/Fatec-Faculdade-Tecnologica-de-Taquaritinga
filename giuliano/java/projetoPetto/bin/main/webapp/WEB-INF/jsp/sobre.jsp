<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="jakarta.tags.core" %>
<jsp:include page="layouttopo.jsp"></jsp:include>

<!-- Seção de Introdução -->
<section id="sobre" class="text-center py-5 bg-light">
    <div class="container">
        <h1 class="display-4 text-dark">Sobre a Petto</h1>
        <p class="lead text-muted">Conheça nossa história, missão e valores. Cuidamos do seu pet com carinho e dedicação!</p>
    </div>
</section>

<!-- Seção de História -->
<section id="historia" class="py-5" style="background-color: white;">
    <div class="container">
        <h2 class="text-center mb-4">Nossa História</h2>
        <p class="text-muted text-center">
            Fundada em 2023, a Petto surgiu com o objetivo de oferecer serviços de qualidade para o cuidado e bem-estar dos animais. 
            Desde então, trabalhamos com amor e dedicação para garantir que cada pet receba a melhor atenção possível.
        </p>
        <div class="row g-4">
            <div class="col-md-6">
                <img src="imagens/historia.jpg" class="img-fluid" alt="História da Petto" style="border-radius: 8px;">
            </div>
            <div class="col-md-6">
                <p>
                    Desde o início, nossa missão tem sido proporcionar serviços especializados para os animais, garantindo um ambiente seguro e acolhedor.
                    Contamos com uma equipe apaixonada por pets e sempre em busca de inovação, para oferecer o melhor para seus amigos de quatro patas.
                </p>
            </div>
        </div>
    </div>
</section>

<!-- Seção de Missão e Valores -->
<section id="missao-valores" class="py-5 bg-light">
    <div class="container">
        <h2 class="text-center mb-4">Missão e Valores</h2>
        <div class="row g-4">
            <!-- Missão -->
            <div class="col-md-6">
                <div class="card h-100 border-0 bg-transparent" style="border-radius: 8px;">
                    <div class="card-body" style="background-color: #f0f8ff; border-radius: 8px;">
                        <h5 class="card-title">Nossa Missão</h5>
                        <p class="card-text">Proporcionar o melhor atendimento para seu pet, com serviços personalizados que garantem sua saúde, segurança e bem-estar.</p>
                    </div>
                </div>
            </div>

            <!-- Valores -->
            <div class="col-md-6">
                <div class="card h-100 border-0 bg-transparent" style="border-radius: 8px;">
                    <div class="card-body" style="background-color: #f5f5dc; border-radius: 8px;">
                        <h5 class="card-title">Nossos Valores</h5>
                        <ul>
                            <li>Respeito e cuidado com os animais</li>
                            <li>Compromisso com a qualidade e inovação</li>
                            <li>Transparência e confiança no atendimento</li>
                            <li>Empatia e dedicação</li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>

<jsp:include page="layoutrodape.jsp"></jsp:include>



