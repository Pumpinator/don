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

function changeStatus() {
    let statusElement = document.getElementById('status');
    let preparingCircle = document.getElementById('preparingCircle');
    let bakingCircle = document.getElementById('bakingCircle');
    let readyCircle = document.getElementById('readyCircle');
    let timeElement = document.getElementById('timeElement'); //muestra la fecha y hora

    // Función para obtener la fecha y hora actual
    function getCurrentDateTime() {
      var now = new Date();
      var hours = now.getHours();
      var minutes = now.getMinutes();
      var ampm = hours >= 12 ? 'p. m.' : 'a. m.';
      hours = hours % 12;
      hours = hours ? hours : 12; // la hora '0' debe ser '12'
      minutes = minutes < 10 ? '0' + minutes : minutes; // Formato de minutos
      var strTime = hours + ':' + minutes + ' ' + ampm;
      var dateString = now.toLocaleDateString('es-ES'); // Fecha en formato local

      return 'Iniciado el ' + dateString + ' a las ' + strTime;
    }

    // Cambiar el texto dependiendo del estado actual
    if (statusElement.innerHTML === "Preparando") {
      statusElement.innerHTML = "Horneando";
      preparingCircle.classList.add('hidden');
      bakingCircle.classList.remove('hidden');
      timeElement.innerHTML = getCurrentDateTime(); // Actualiza la fecha y hora al iniciar el horneado
    } else if (statusElement.innerHTML === "Horneando") {
      statusElement.innerHTML = "Listo";
      bakingCircle.classList.add('hidden');
      readyCircle.classList.remove('hidden');
    } else if (statusElement.innerHTML === "Listo") {
      statusElement.innerHTML = "Preparando";
      readyCircle.classList.add('hidden');
      preparingCircle.classList.remove('hidden');
    }
  }

function startPreparation() {
    closeModal();

    // Cambia el estado de la tarjeta a "Preparando"
    document.getElementById('status').innerHTML = "Preparando";
}