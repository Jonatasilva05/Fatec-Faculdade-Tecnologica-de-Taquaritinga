<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="jakarta.tags.core" %>
<jsp:include page="layouttopo.jsp"></jsp:include>
	<div class="row">
		<h1>Lista de Livros</h1>
	</div>
	<div class="row">	
		<table class="table table-striped">
			<thead>
				<tr>
					<th>Código</th>
					<th>Titulo</th>
					<th>Editora</th>
					<th>Ano</th>
				</tr>
			</thead>
			<tbody>
				<c:forEach items="${listaLivros}" var="livro">
					<tr>
						<td>${livro.getCodigo()}</td>
						<td>${livro.getTitulo()}</td>
						<td>${livro.getEditora()}</td>
						<td>${livro.getAno()}</td>
					</tr>
				</c:forEach>
			</tbody>
		</table>
	</div>
<jsp:include page="layoutrodape.jsp"></jsp:include>