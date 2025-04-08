<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="jakarta.tags.core" %>
<jsp:include page="layouttopo.jsp"></jsp:include>
	<div class="row">
		<h3>Integrantes do Grupo</h3>	
		<p>
			Stefani, maicon, Jonatas
		</p>
	</div>

	<div vw class="enabled">
		<div vw-access-button class="active"></div>
		<div vw-plugin-wrapper>
		  <div class="vw-plugin-top-wrapper"></div>
		</div>
	</div>

	<script src="https://vlibras.gov.br/app/vlibras-plugin.js"></script>
  	<script>
    	new window.VLibras.Widget('https://vlibras.gov.br/app');
  	</script>

<section class="container my-5">
    <div class="row">
      <div class="col-md-6">
        <h2 class="text-uppercase mb-3">
          <span class="text-pt">Bem-vindo à Petto</span>
          <span class="text-en hidden">Welcome to Petto</span>
          <span class="text-es hidden">¡Bienvenido a Petto!</span>
        </h2>

        <p>
          <span class="text-pt">A Petto oferece uma gama de serviços que garantem o bem-estar do seu animal de estimação, desde passeios com cães até vacinação e consultoria de saúde. Nosso objetivo é cuidar do seu pet com amor e dedicação.</span>
          <span class="text-en hidden">Petto offers a range of services that ensure the well-being of your pet, from dog walking to vaccination and health consulting. Our goal is to care for your pet with love and dedication.</span>
          <span class="text-es hidden">Petto ofrece una gama de servicios que garantizan el bienestar de tu mascota, desde paseos para perros hasta vacunación y consultoría de salud. Nuestro objetivo es cuidar de tu mascota con amor y dedicación.</span>
        </p>

        <ul class="list-unstyled">
          <li>
            <i class="fas fa-check-circle text-success me-2"></i>
            <span class="text-pt">Serviços de Dogwalk com horários flexíveis</span>
            <span class="text-en hidden">Dog walking services with flexible hours</span>
            <span class="text-es hidden">Servicios de paseo para perros con horarios flexibles</span>
          </li>
          <li>
            <i class="fas fa-check-circle text-success me-2"></i>
            <span class="text-pt">Carteira de vacinação digital para facilitar o acompanhamento</span>
            <span class="text-en hidden">Digital vaccination card for easy tracking</span>
            <span class="text-es hidden">Cartilla de vacunación digital para un mejor seguimiento</span>
          </li>
          <li>
            <i class="fas fa-check-circle text-success me-2"></i>
            <span class="text-pt">Consultoria especializada em saúde pet</span>
            <span class="text-en hidden">Specialized pet health consulting</span>
            <span class="text-es hidden">Consultoría especializada en salud para mascotas</span>
          </li>
        </ul>

        <a href="" class="btn btn-dark ms-3">
          <span class="text-pt">Saiba mais sobre nossos serviços</span>
          <span class="text-en hidden">Learn more about our services</span>
          <span class="text-es hidden">[Descubre más sobre nuestros servicios]</span>
        </a>

      </div>

      <div class="col-md-6">
        <img src="img/p1/i1.jpg" class="img-fluid rounded" alt="Imagem de pets felizes">
      </div>

    </div>
  </section>

<jsp:include page="layoutrodape.jsp"></jsp:include>