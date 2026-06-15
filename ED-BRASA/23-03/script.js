// let mostrarMensagem = function(){
//         document.write("Olá")
//     }
//     mostrarMensagem()

// let funcao = function(){
//         somar(1, 2)
//     }
//     function somar(p1, p2){
//         let res = p1 + p2
//         document.write("<br> A soma é: " + res)
//     }
//     funcao()

let somarValores = function() {
    let valor1 = parseInt(document.getElementById("txtValor1").value);
    let valor2 = parseInt(document.getElementById("txtValor2").value);

    if (isNaN(valor1) || isNaN(valor2)) {
        alert("Por favor, insira os dois valores.");
        return;
    }

    const loader = document.getElementById("loader");
    const mensagem = loader.querySelector("p");
    const resultadoDiv = document.getElementById("resultado");
    const formArea = document.getElementById("formArea");

    resultadoDiv.classList.remove("mostrar");

    loader.style.display = "flex";
    mensagem.innerText = "Realizando operação...";

    setTimeout(() => {
        let resultado = valor1 + valor2;

        loader.style.display = "none";
        formArea.style.display = "none";

        resultadoDiv.innerHTML = "A soma é: " + resultado;
        resultadoDiv.offsetHeight;
        resultadoDiv.classList.add("mostrar");

        setTimeout(() => {
            loader.style.display = "flex";
            mensagem.innerText = "Recarregando a página...";

            setTimeout(() => {
                location.reload();
            }, 2000);

        }, 2500);

    }, 1500);
}