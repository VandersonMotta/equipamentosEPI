
//método para menu accordion
var acc = document.getElementsByClassName("accordion");
for (var i = 0; i < acc.length; i++) {
    acc[i].addEventListener("click", function () {
        this.classList.toggle("active");
        var panel = this.nextElementSibling;
        if (panel.style.display === "block") {
            panel.style.display = "none";
        } else {
            panel.style.display = "block";
        }
    });
}

//método para exibição do conteúdo baseado no submenu clicado
document.querySelectorAll(".panel a").forEach(item => {
    item.addEventListener("click", function () {
        // Esconde todas as caixas de conteúdo
        document.querySelectorAll(".content-box").forEach(box => {
            box.classList.add("hidden");
        });

        // Obtém o valor de data-target e exibe o conteúdo correspondente
        var targetId = this.getAttribute("data-target");
        document.getElementById(targetId).classList.remove("hidden");
    });
});

const statusField = document.getElementById("id_status");
const observacaoDiv = document.getElementById("div-observacao");
const devolucaoDiv = document.getElementById("div-devolucao");

function toggleCamposExtras() {
    const valor = statusField.value;
    if (valor === "devolvido" || valor === "danificado" || valor === "perdido") {
        observacaoDiv.style.display = "block";
        devolucaoDiv.style.display = "block";
    } else {
        observacaoDiv.style.display = "none";
        devolucaoDiv.style.display = "none";
    }
}

/*GRAFICO*/
// Função para configurar o gráfico
function createChart(epiData) {
    // Rótulos para os status
    const labels = ['Emprestado', 'Em Uso', 'Fornecido', 'Devolvido', 'Danificado', 'Perdido'];
    const data = [0, 0, 0, 0, 0, 0];

    // Somando as quantidades para cada status
    epiData.forEach(epi => {
        data[0] += epi.status_counts.emprestado || 0; // Emprestado
        data[1] += epi.status_counts.em_uso || 0;     // Em Uso
        data[2] += epi.status_counts.fornecido || 0;   // Fornecido
        data[3] += epi.status_counts.devolvido || 0;   // Devolvido
        data[4] += epi.status_counts.danificado || 0;  // Danificado
        data[5] += epi.status_counts.perdido || 0;     // Perdido
    });

    // Selecionando o canvas para o gráfico
    const ctx = document.getElementById('epiChart').getContext('2d');

    // Criando o gráfico de rosca
    new Chart(ctx, {
        type: 'doughnut', // Tipo de gráfico rosca
        data: {
            labels: labels,  // Labels para cada status
            datasets: [{
                label: 'Status de EPI',
                data: data,  // Dados a serem exibidos no gráfico
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 206, 86, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)',
                    'rgba(255, 159, 64, 0.2)'
                ],
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(255, 159, 64, 1)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            responsive: true, // Gráfico responsivo
            plugins: {
                legend: {
                    position: 'top', // Posição da legenda
                },
                tooltip: {
                    callbacks: {
                        label: function(tooltipItem) {
                            // Exibe o valor de cada status ao passar o mouse
                            const label = tooltipItem.label || '';
                            const value = tooltipItem.raw || 0;
                            return `${label}: ${value}`;
                        }
                    }
                }
            }
        }
    });
}

// Obtendo os dados passados pelo Django
const epiData = JSON.parse(document.getElementById('epi-data').textContent);

// Chama a função para criar o gráfico com os dados
createChart(epiData);
