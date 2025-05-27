<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="jakarta.tags.core" %>
<jsp:include page="layouttopo.jsp"></jsp:include>
    <c:set var="valor" value="1"></c:set>
    <c:if test="${valor == 1}">
        <b>Ok</b>
    </c:if>
	<div class="row">
        <h1>Contato</h1>
        <ul>
            <c:forEach items="${listaContatos}" var="contato">
                <li>${contato}</li>
            </c:forEach>
        </ul>
	</div>
<jsp:include page="layoutrodape.jsp"></jsp:include>