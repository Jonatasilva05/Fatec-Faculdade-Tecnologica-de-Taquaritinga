<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="jakarta.tags.core" %>
<%@ taglib prefix="form" uri="http://www.springframework.org/tags/form" %>
<jsp:include page="layouttopo.jsp"></jsp:include>
    <div class="row">
        <h1>Cadastrar Livro</h1>
    </div>
    <div class="row">
        <form:form action="/cadastrar" modelAttribute="livro">
            <div class="mb-3">
                <label for="titulo" class="form-label">Título:</label>
                <input type="text" class="form-control" name="titulo" maxlength="100" required/>
              </div>
              <div class="mb-3">
                <label for="editora" class="form-label">Editora:</label>
                <input type="text" class="form-control" name="editora" maxlength="50" required/>
              </div>
              <div class="mb-3">
                <label for="ano" class="form-label">Ano:</label>
                <input type="number" class="form-control" name="ano" required/>
              </div>              
              <button type="submit" class="btn btn-primary">Cadastrar</button>        
        </form:form>
    </div>
<jsp:include page="layoutrodape.jsp"></jsp:include>