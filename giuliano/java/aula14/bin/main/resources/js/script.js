$(document).ready(()=> {
    $('#tabela').on('click', '.excluir', (evento)=> {
        let codigo = evento.target.getAttribute('rel');
        if(confirm('Tem certeza que deseja excluir o livro?')) {
            let url = 'http://localhost:9000/excluirlivro?codigo='+ codigo;
            
        }
    });
});