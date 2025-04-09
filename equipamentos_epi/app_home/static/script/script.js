
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

