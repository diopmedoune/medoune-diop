const navbarLinks = document.querySelectorAll('.navbar a');

navbarLinks.forEach(link => {
    if (link.href === window.location.href) {
        link.classList.add('active');
    }
});
