$(document).ready(()=> {
    $('#tabela').on('click', '.excluir', (evento)=> {
        let codigo = evento.target.getAttribute('rel');
        alert(codigo);  
    });
});