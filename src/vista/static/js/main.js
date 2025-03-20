document.querySelectorAll('[data-dismiss-target]').forEach((btn) => {
    btn.addEventListener('click', function () {
        const targetSelector = this.getAttribute('data-dismiss-target');
        const targetEl = document.querySelector(targetSelector);
        if (targetEl) {
            targetEl.classList.add('hidden');
        }
    });
});