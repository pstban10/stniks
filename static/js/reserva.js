document.getElementById('date').addEventListener('change', function () {
    const fecha = this.value;
    const diaSemana = obtenerDiaSemana(fecha);

    fetch(`horarios/?dia=${diaSemana}`)
        .then(response => response.json())
        .then(data => {
            const hourSelect = document.getElementById('hour');
            hourSelect.innerHTML = '';  // Limpiar opciones existentes

            data.horarios.forEach(horario => {
                const option = document.createElement('option');
                option.value = horario;
                option.textContent = horario;
                hourSelect.appendChild(option);
            });
        })
        .catch(error => console.error('Error:', error));
});

function obtenerDiaSemana(fecha) {
    const diasSemana = ['domingo', 'lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado'];
    const fechaObj = new Date(fecha);
    const diaSemana = diasSemana[fechaObj.getUTCDay()];
    return diaSemana;
}
