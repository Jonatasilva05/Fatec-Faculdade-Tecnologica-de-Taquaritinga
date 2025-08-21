<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="jakarta.tags.core" %>
<jsp:include page="layouttopo.jsp"></jsp:include>
	<div class="row">
		<h1>Cadastrar Livro</h1>
	</div>

	<div class="row">
		<form>
            <div class="mb-3">
              <label for="examploTituloLivro" class="form-label">Titulo: </label>
              <input type="text" class="form-control" id="examploTituloLivro" aria-describedby="tituloHelp">
              <div id="tituloHelp" class="form-text">Por favor, coloque o titulo do Livro a ser cadastrado</div>
            </div>
            <div class="mb-3">
              <label for="exemploEditora" class="form-label">Editora: </label>
              <input type="text" class="form-control" id="exemploEditora" aria-describedby="editoraHelp">
              <div id="editoraHelp" class="form-text">Por favor, coloque a editora do Livro</div>
            </div>
            <div class="mb-3">
              <label for="anoLivro" class="form-label">Editora: </label>
              <input type="date" class="form-control" id="anoLivro" aria-describedby="anoHelp">
              <div id="anoHelp" class="form-text">Por favor, coloque o ano do Livro</div>
            </div>
            <button type="submit" class="btn btn-primary">Cadastrar Livro</button>
        </form>
	</div>
<jsp:include page="layoutrodape.jsp"></jsp:include>