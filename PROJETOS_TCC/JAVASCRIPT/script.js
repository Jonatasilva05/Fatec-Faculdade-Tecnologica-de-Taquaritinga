document.addEventListener('DOMContentLoaded', function() {
    const header = document.querySelector('header');
    let lastScrollTop = 0;
    window.addEventListener('scroll', () => {
        let scrollTop = window.pageYOffset || document.documentElement.scrollTop;

        if (scrollTop > lastScrollTop) {
            // Scroll para baixo
            header.classList.add('hide-on-scroll');
        } else {
            // Scroll para cima
            header.classList.remove('hide-on-scroll');
        }
        lastScrollTop = scrollTop;
    });
});
