document.getElementById('menu-toggle').addEventListener('click', function() {
    const sidebar = document.getElementById('sidebar-wrapper');
    const mainContent = document.getElementById('page-content-wrapper');
    const menu = document.getElementById('menu_open');
    const menu_hidden = document.getElementById('menu_collapsed');
    const name = document.getElementById('Main_name');
    sidebar.classList.toggle('collapsed');
    mainContent.classList.toggle('collapsed');
    menu.classList.toggle('collapsed');
    menu_hidden.classList.toggle('collapsed');
    name.classList.toggle('collapsed');
});

const menuLinks = document.querySelectorAll('.menu-item');
menuLinks.forEach(link => {
    link.addEventListener('click', function(event) {
        event.preventDefault();
        const sidebar = document.getElementById('sidebar-wrapper');
        sidebar.classList.remove('collapsed');
        // Here you would add logic to navigate to the correct page
        // For demonstration, just log the clicked menu item
        console.log(`Navigating to: ${link.textContent.trim()}`);
    });
});
