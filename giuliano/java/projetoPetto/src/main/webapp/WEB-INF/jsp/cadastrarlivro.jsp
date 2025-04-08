<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="jakarta.tags.core" %>

<jsp:include page="layouttopo.jsp"></jsp:include>
<div class="row">
    <h1 class="titulo-centralizado">Cadastrar Livro</h1>
</div>
<div class="row form-cadastro-livro">
    <form action="cadastrarLivro" method="post">
        <div class="form-group">
            <label for="titulo">Título:</label>
            <input type="text" class="form-control" id="titulo" name="titulo" required>
        </div>
        <div class="form-group">
            <label for="editora">Editora:</label>
            <input type="text" class="form-control" id="editora" name="editora" required>
        </div>
        <div class="form-group">
            <label for="ano">Ano de Publicação:</label>
            <input type="number" class="form-control" id="ano" name="ano" required>
        </div>
        <button type="submit" class="btn btn-primary">Cadastrar</button>
    </form>
</div>
<jsp:include page="layoutrodape.jsp"></jsp:include>

