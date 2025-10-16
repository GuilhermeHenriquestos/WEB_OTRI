document.addEventListener('DOMContentLoaded', function() {
    // Seleciona todos os links de navegação e as seções de conteúdo
    const navItems = document.querySelectorAll('.sidebar-nav .nav-item');
    const contentSections = document.querySelectorAll('.content-section');

    // Adiciona um "ouvinte de evento" de clique a cada link de navegação
    navItems.forEach(item => {
        item.addEventListener('click', function(event) {
            // Previne o comportamento padrão do link (que seria recarregar a página)
            event.preventDefault();
            
            // Obtém o ID da seção de destino a partir do atributo data-target
            const targetId = this.getAttribute('data-target');

            // Remove a classe 'active' de todos os links de navegação
            navItems.forEach(nav => nav.classList.remove('active'));
            // Adiciona a classe 'active' ao link clicado
            this.classList.add('active');

            // Remove a classe 'active' de todas as seções de conteúdo
            contentSections.forEach(section => section.classList.remove('active'));

            // Mostra a seção de conteúdo correspondente adicionando a classe 'active'
            const targetView = document.getElementById(targetId);
            if (targetView) {
                targetView.classList.add('active');
            }
        });
    });
});