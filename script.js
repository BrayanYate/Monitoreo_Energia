/// Consumo general
const consumoData = {
  labels: ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun'],
  datasets: [{
    label: 'Consumo (kWh)',
    data: [120, 150, 135, 180, 160, 140],
    backgroundColor: 'rgba(75, 192, 192, 0.2)',
    borderColor: 'rgba(75, 192, 192, 1)',
    borderWidth: 1
  }]
};
// Consumo diario
const consumoDiarioData = {
  labels: ['00:00', '03:00', '06:00', '09:00', '12:00', '15:00', '18:00', '21:00'],
  datasets: [{
    label: 'Consumo Diario (kWh)',
    data: [2, 1, 0.5, 3, 5, 4, 3.5, 2.5],
    fill: false,
    borderColor: 'rgba(255, 99, 132, 1)',
    tension: 0.1
  }]
};

const ctxDiario = document.getElementById('consumoDiarioChart').getContext('2d');
new Chart(ctxDiario, {
  type: 'line',
  data: consumoDiarioData,
});

//Consumo por electrodomesticos
const consumoElectrodomesticosData = {
  labels: ['Refrigerador', 'Lavadora', 'Aire acondicionado', 'Televisor', 'Otros'],
  datasets: [{
    data: [30, 20, 25, 10, 15],
    backgroundColor: [
      'rgba(255, 99, 132, 0.2)',
      'rgba(54, 162, 235, 0.2)',
      'rgba(255, 206, 86, 0.2)',
      'rgba(75, 192, 192, 0.2)',
      'rgba(153, 102, 255, 0.2)'
    ]
  }]
};

// Crear el gráfico
const ctxElectrodomesticos = document.getElementById('consumoElectrodomesticosChart').getContext('2d');
new Chart(ctxElectrodomesticos, {
  type: 'doughnut',
  data: consumoElectrodomesticosData,
});

// Consumo mes anterior
const consumoComparacionData = {
  labels: ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun'],
  datasets: [{
    label: 'Consumo actual (kWh)',
    data: [120, 150, 135, 180, 160, 140],
    backgroundColor: 'rgba(75, 192, 192, 0.2)',
    borderColor: 'rgba(75, 192, 192, 1)',
    borderWidth: 1
  },
  {
    label: 'Consumo mes anterior (kWh)',
    data: [130, 145, 120, 170, 155, 135],
    backgroundColor: 'rgba(255, 99, 132, 0.2)',
    borderColor: 'rgba(255, 99, 132, 1)',
    borderWidth: 1
  }]
};

// Crear el gráfico
const ctxComparacion = document.getElementById('consumoComparacionChart').getContext('2d');
new Chart(ctxComparacion, {
  type: 'bar',
  data: consumoComparacionData,
});


const alertas = [
  'Consumo alto en abril',
  'Reducción del consumo en junio'
];

const ctx = document.getElementById('consumoChart').getContext('2d');
new Chart(ctx, {
  type: 'bar',
  data: consumoData,
});

const listaAlertas = document.getElementById('listaAlertas');
alertas.forEach(alerta => {
  const div = document.createElement('div');
  div.classList.add('alert');
  if (alerta.includes('alto')) {
    div.classList.add('alert-danger');
  } else if (alerta.includes('Reducción')) {
    div.classList.add('alert-warning');
  }
  div.setAttribute('role', 'alert');
  div.textContent = alerta;
  listaAlertas.appendChild(div);
});

const sugerencias = [
  'Apaga las luces cuando no las estés utilizando',
  'Utiliza bombillas de bajo consumo energético',
  'Aprovecha la luz natural en lugar de encender las luces',
  'Desconecta los electrodomésticos cuando no los estés utilizando',
  'Utiliza electrodomésticos eficientes en energía',
  'Ajusta la temperatura del aire acondicionado o calefacción a niveles adecuados',
  'Utiliza cortinas o persianas para regular la temperatura de tu hogar',
  'Realiza un uso responsable de la lavadora y el lavavajillas',
  'Evita dejar los dispositivos electrónicos en modo de espera',
  'Aprovecha la energía solar para calentar agua o generar electricidad'
];

const listaSugerencias = document.getElementById('listaSugerencias');
sugerencias.forEach(sugerencias => {
  const li = document.createElement('li');
  li.textContent = sugerencias;
  listaSugerencias.appendChild(li);
});