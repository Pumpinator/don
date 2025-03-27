document.querySelectorAll('[data-dismiss-target]').forEach((btn) => {
    btn.addEventListener('click', function() {
        const targetSelector = this.getAttribute('data-dismiss-target');
        const targetEl = document.querySelector(targetSelector);
        if (targetEl) {
            targetEl.classList.add('hidden');
        }
    });
});

function showTab(tabName) {
    // Ocultar todos los contenidos
    document.getElementById('insumos-content').classList.add('hidden');
    document.getElementById('galletas-content').classList.add('hidden');
    document.getElementById('produccion-content').classList.add('hidden');

    // Resetear todos los botones
    document.getElementById('insumos-tab').classList.remove('bg-white');
    document.getElementById('insumos-tab').classList.add('bg-gray-200');
    document.getElementById('galletas-tab').classList.remove('bg-white');
    document.getElementById('galletas-tab').classList.add('bg-gray-200');
    document.getElementById('produccion-tab').classList.remove('bg-white');
    document.getElementById('produccion-tab').classList.add('bg-gray-200');

    // Mostrar el contenido seleccionado
    document.getElementById(tabName + '-content').classList.remove('hidden');

    // Resaltar el botón seleccionado
    document.getElementById(tabName + '-tab').classList.remove('bg-gray-200');
    document.getElementById(tabName + '-tab').classList.add('bg-white');
}

// Mostrar insumos por defecto
document.addEventListener('DOMContentLoaded', function() {
    showTab('insumos');
});