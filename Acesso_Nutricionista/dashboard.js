document.addEventListener('DOMContentLoaded', function() {
    // 1. Navegação da Barra Lateral
    const navItems = document.querySelectorAll('.sidebar-nav .nav-item');
    const contentSections = document.querySelectorAll('.content-section');

    navItems.forEach(item => {
        item.addEventListener('click', function(event) {
            event.preventDefault();
            
            const targetId = this.getAttribute('data-target');

            navItems.forEach(nav => nav.classList.remove('active'));
            this.classList.add('active');

            contentSections.forEach(section => section.classList.remove('active'));
            document.getElementById(targetId).classList.add('active');
        });
    });

    // 2. Botão "Cadastrar Cliente" no Dashboard
    const newClientBtn = document.querySelector('.btn-primary[data-target="new-client"]');
    if (newClientBtn) {
        newClientBtn.addEventListener('click', function(event) {
            event.preventDefault();
            // Desativa o item atual e ativa "Cadastrar Cliente"
            document.querySelector('.nav-item.active').classList.remove('active');
            document.querySelector('.nav-item[data-target="new-client"]').classList.add('active');
            
            // Esconde a seção atual e mostra a de cadastro
            document.querySelector('.content-section.active').classList.remove('active');
            document.getElementById('new-client').classList.add('active');
        });
    }

    // 3. Botão "Visualizar Chat"
    const viewChatBtns = document.querySelectorAll('.btn-view-chat');
    viewChatBtns.forEach(btn => {
        btn.addEventListener('click', function() {
            // Lógica para ir para a tela de chat
            const clientName = btn.closest('.client-item').querySelector('span').textContent;
            
            // Esconde a seção atual e mostra a de chat
            document.querySelector('.content-section.active').classList.remove('active');
            document.getElementById('chat-view').classList.add('active');

            // Atualiza o título da seção de chat com o nome do cliente
            document.querySelector('#chat-view .section-header h2').textContent = `Chat com ${clientName}`;

            // Efeito visual na navegação lateral
            document.querySelector('.nav-item.active').classList.remove('active');
            document.querySelector('.nav-item[data-target="dashboard"]').classList.add('active');
        });
    });
    
    // 4. Seleção de Cor do Bot
    const colorBoxes = document.querySelectorAll('.color-box');
    colorBoxes.forEach(box => {
        box.addEventListener('click', function() {
            colorBoxes.forEach(c => c.classList.remove('selected'));
            this.classList.add('selected');
            const selectedColor = this.getAttribute('data-color');
            console.log(`Cor selecionada para o bot: ${selectedColor}`);
        });
    });
});