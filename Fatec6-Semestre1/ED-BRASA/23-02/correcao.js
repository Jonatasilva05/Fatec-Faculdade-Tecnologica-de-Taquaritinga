document.getElementById('meuFormulario').addEventListener('submit', function(event) {
        let nome = document.getElementById('codigo').value;
        if (nome.trim() == 1) {
            alert("Chaves");
            event.preventDefault();
        }
        else if (nome.trim() == 2) {
            alert("Quico");
            event.preventDefault();
        }
        else if (nome.trim() == 3) {
            alert("Dona Florinda");
            event.preventDefault();
        }
        else if (nome.trim() == 4) {
            alert("Seu Madruga");
            event.preventDefault();
        }
        else{
            alert("Insira um codigo valido! Tente Novamente");
        }
    });

    // METODO DO PROFESSOR 
    let codigo 
    codigo = Number(window.prompt("Digite o Código: "));
    if (codigo == 1) {
        document.write("Chaves");
    }
    else if (codigo == 2) {
        document.write("Quico");
    }
    else if (codigo == 3) {
        document.write("Dona Florinda");
    }
    else if (codigo == 4) {
        document.write("Seu Madruga");
    }
    else {
        document.write("Código inválido");
    };

document.getElementById('form2').addEventListener('submit', function(event) {
    let valor = document.getElementById('codigo2').value;
    if (valor.trim() % 2 === 0) {
        alert("Par");
        event.preventDefault();
    }
    else{
        alert("Impar");
    }
});

let resultado = "";
    for (let i = 0; i < 10; i++) {
        resultado += "\n Fatec Taquaritinga";
    }
    console.log(resultado);