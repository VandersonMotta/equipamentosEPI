
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

statusField.addEventListener("change", toggleCamposExtras);
document.addEventListener("DOMContentLoaded", toggleCamposExtras);

function toggleUserMenu() {
    const menu = document.getElementById("user-dropdown");
    menu.style.display = menu.style.display === "block" ? "none" : "block";
}

window.addEventListener("click", function (e) {
    const dropdown = document.getElementById("user-dropdown");
    const userMenu = document.querySelector(".user-menu");

    if (!userMenu.contains(e.target)) {
        dropdown.style.display = "none";
    }
});
