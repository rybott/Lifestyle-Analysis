document.getElementById('menu-toggle').addEventListener('click', function() {
    const sidebar = document.getElementById('sidebar-wrapper');
    const mainContent = document.getElementById('page-content-wrapper');
    sidebar.classList.toggle('collapsed');
    mainContent.classList.toggle('collapsed');
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
