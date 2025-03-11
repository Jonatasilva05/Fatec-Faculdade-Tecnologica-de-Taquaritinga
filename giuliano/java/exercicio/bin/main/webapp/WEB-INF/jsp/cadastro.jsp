<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="jakarta.tags.core" %>
<jsp:include page="layouttopo.jsp"></jsp:include>
    <div class="row">
        <form action="">
            <label for="name">Nome:</label>
                <input type="text" name="name" id="name" placeholder="Digite o seu nome">  
                <br><br>
            <label for="email">E-mail:</label>
                <input type="email" name="email" id="email" placeholder="Digite o seu E-mail">
                <br><br>
            <label for="password">Senha:</label>
                <input type="password" name="password" id="password" placeholder="Digite a sua senha">
                <br><br>
            <label for="password">Confirmação de Senha:</label>
                <input type="password" name="password" id="password" placeholder="Digite a sua senha novamente">
                <br><br>
                <button type="submit">Enviar</button>
        </form>
    </div>

<jsp:include page="layoutrodape.jsp"></jsp:include>