<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="jakarta.tags.core" %>
<jsp:include page="layouttopo.jsp"></jsp:include>
    <div class="row">
        <form action="">
            <div class="h1">
                <h1>Login</h1>
            </div>
            <label for="">Faça seu Login para acessar a sua conta</label>
                <br>
            <div class="PrimEntDados">
                <label for="">Usuario</label>
                <input type="text" placeholder="Digite seu Usuário">
            </div>
                <br>
            <div class="PrimEntDados">
                <label for="">Senha</label>
                <input type="password" placeholder="Digite sua Senha">
            </div>

            <hr><hr>

            <button>Entrar</button>

            <hr><hr>

            <a href="#">Esqueceu a Senha?</a>
        </form>
    </div>

<jsp:include page="layoutrodape.jsp"></jsp:include>