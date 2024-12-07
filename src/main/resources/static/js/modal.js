function openModal() {
    document.getElementById('modal').classList.remove('hidden');
    document.body.classList.add('modal-open');
    document.getElementById('mainContent').classList.add('blur');
}

function closeModal() {
    document.getElementById('modal').classList.add('hidden');
    document.body.classList.remove('modal-open');
    document.getElementById('mainContent').classList.remove('blur');
}