window.onscroll = () => {
    scroll();
};

function scroll() {
    const footer = document.querySelector('footer');
    const rect = footer.getBoundingClientRect();
    const isVisible = rect.top < window.innerHeight && rect.bottom >= 0;
    const button = document.getElementById('volverArriba');

    if (isVisible) {
        button.classList.remove('hidden');
    } else {
        button.classList.add('hidden');
    }
}