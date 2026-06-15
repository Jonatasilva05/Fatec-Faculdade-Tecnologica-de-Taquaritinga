// Obter o link e a div de carregamento
const link = document.getElementById('link');
const loading = document.getElementById('loading');

// Adicionar evento de clique no link
link.addEventListener('click', (event) => {
    // Prevenir o comportamento padrão do link (que vai para a página imediatamente)
    event.preventDefault();

    // Mostrar a tela de carregamento
    loading.style.display = 'flex';

    // Aguardar 0.2 segundos e depois redirecionar para a nova página
    setTimeout(() => {
        // Redirecionar para a nova página
        window.location.href = link.href;
    }, 200); // 0.2 segundos
});

// Evento para esconder o efeito de carregamento quando a nova página for carregada
window.addEventListener('load', () => {
    loading.style.display = 'none';
});
