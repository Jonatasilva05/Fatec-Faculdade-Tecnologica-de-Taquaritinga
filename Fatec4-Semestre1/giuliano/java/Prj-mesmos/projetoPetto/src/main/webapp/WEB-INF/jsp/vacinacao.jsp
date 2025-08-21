<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="jakarta.tags.core" %>
<jsp:include page="layouttopo.jsp"></jsp:include>
  
 <!-- Seção de Introdução -->
 <section id="introducao" class="text-center py-5 bg-light">
    <div class="container">
        <h1 class="display-4 section-title">Carteira de Vacinação</h1>
        <p class="lead text-muted">A carteira de vacinação é essencial para garantir a saúde e bem-estar do seu pet. Ela contém todas as vacinas que seu animal recebeu e é fundamental para seu controle de saúde.</p>
    </div>
</section>

<!-- O que é a Carteira de Vacinação -->
<section id="o-que-e" class="py-5">
    <div class="container">
        <h2 class="text-center section-title">O que é a Carteira de Vacinação?</h2>
        <div class="row">
            <div class="col-md-6">
                <div class="card mb-4">
                    <div class="card-body">
                        <h5 class="card-title">Definição</h5>
                        <p>A carteira de vacinação é um documento oficial que registra todas as vacinas administradas ao seu pet. Ela é essencial para comprovar que o animal está devidamente protegido contra doenças perigosas.</p>
                        <p>Além disso, é um meio de controle tanto para o dono quanto para o veterinário, que podem acompanhar o histórico vacinal e tomar decisões de cuidados com base nas informações dessa carteira.</p>
                    </div>
                </div>
            </div>
            <div class="col-md-6">
                <img src="https://via.placeholder.com/500x300" alt="Imagem da Carteira de Vacinação" class="img-fluid rounded">
            </div>
        </div>
    </div>
</section>

<!-- Importância da Vacinação -->
<section id="importancia" class="py-5 bg-light">
    <div class="container">
        <h2 class="text-center section-title">Por que a Vacinação é Importante?</h2>
        <div class="row">
            <div class="col-md-6">
                <div class="card">
                    <div class="card-body">
                        <p>A vacinação é uma das medidas mais eficazes para prevenir doenças graves e até fatais. Ela ajuda a proteger não apenas o seu pet, mas também outras pessoas e animais ao seu redor.</p>
                        <ul>
                            <li><strong>Prevenção:</strong> As vacinas evitam que seu pet contraia doenças infecciosas.</li>
                            <li><strong>Segurança:</strong> Protege contra doenças transmissíveis que podem afetar outros animais.</li>
                            <li><strong>Obrigatoriedade:</strong> Em muitos lugares, a vacinação é exigida para animais de estimação.</li>
                        </ul>
                    </div>
                </div>
            </div>
            <div class="col-md-6 text-center">
                <i class="fas fa-shield-alt fa-5x text-primary mb-3"></i>
                <p class="lead">Vacinar seu pet é um ato de cuidado e responsabilidade.</p>
            </div>
        </div>
    </div>
</section>

<!-- Vacinas Essenciais -->
<section id="vacinas" class="py-5">
    <div class="container">
        <h2 class="text-center section-title">Vacinas Essenciais</h2>
        <div class="row">
            <div class="col-md-4">
                <div class="card">
                    <div class="card-body text-center">
                        <i class="fas fa-paw fa-3x text-success mb-3"></i>
                        <h5 class="card-title">Vacina V8 / V10</h5>
                        <p class="card-text">Vacina polivalente para cães que protege contra doenças como parvovirose, cinomose, hepatite, leptospirose, entre outras.</p>
                    </div>
                </div>
            </div>
            <div class="col-md-4">
                <div class="card">
                    <div class="card-body text-center">
                        <i class="fas fa-syringe fa-3x text-danger mb-3"></i>
                        <h5 class="card-title">Raiva</h5>
                        <p class="card-text">Vacina contra a raiva, uma doença fatal e transmissível aos humanos. Essencial para todos os cães e gatos.</p>
                    </div>
                </div>
            </div>
            <div class="col-md-4">
                <div class="card">
                    <div class="card-body text-center">
                        <i class="fas fa-heart fa-3x text-info mb-3"></i>
                        <h5 class="card-title">Leishmaniose</h5>
                        <p class="card-text">Vacina contra a leishmaniose, uma doença transmitida por flebótomos. Importante para áreas endêmicas.</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- Como Atualizar a Carteira -->
<section id="como-atualizar" class="py-5 bg-light">
    <div class="container">
        <h2 class="text-center section-title">Como Atualizar a Carteira de Vacinação?</h2>
        <p class="text-center">A carteira de vacinação do seu pet deve ser atualizada conforme o cronograma de vacinas indicado pelo veterinário. Normalmente, as vacinas têm uma validade de um ano, e o veterinário deve registrar a aplicação e a data de validade de cada vacina na carteira.</p>
        <ul>
            <li>Visite o veterinário regularmente.</li>
            <li>Fique atento às datas de reforço das vacinas.</li>
            <li>Guarde a carteira de vacinação em local seguro e de fácil acesso.</li>
        </ul>
    </div>
</section>

<!-- Conclusão -->
<section id="conclusao" class="py-5">
    <div class="container text-center">
        <h2 class="section-title">Manter a Carteira de Vacinação em Dia é Essencial!</h2>
        <p class="lead">A vacinação é um compromisso contínuo com a saúde do seu pet. Ao manter a carteira de vacinação atualizada, você garante o bem-estar do seu animal e ajuda na prevenção de doenças.</p>
        <a href="https://www.exemplo-veterinario.com" class="btn btn-info btn-lg"><i class="fas fa-veterinarian"></i> Agende uma consulta</a>
    </div>
</section>

<jsp:include page="layoutrodape.jsp"></jsp:include>


