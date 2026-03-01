const navLinks = document.querySelectorAll('.close-navbar');
const navbarToggler = document.querySelector('.navbar-toggler');
const navbarCollapse = document.querySelector('.navbar-collapse');

navLinks.forEach(link => {
    link.addEventListener('click', function () {
        if (window.getComputedStyle(navbarToggler).display !== 'none') {
            const bsCollapse = new bootstrap.Collapse(navbarCollapse, {
                toggle: false
            });
            bsCollapse.hide();
        }
    });
});

function showPopup(title,message) {
    const Container = document.getElementById('PopupMsg');
    const modal_title = Container.querySelector('.modal-title');
    const modal_body = Container.querySelector('.modal-body');
    console.log('working');
    if (modal_title) modal_title.innerText = title;
    if (modal_body) modal_body.innerText = message;
    
    const modal = bootstrap.Modal.getOrCreateInstance(Container) || new bootstrap.Modal(Container);
    modal.show();
}
