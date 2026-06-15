function checkNum(){
    const input = document.getElementById('numero').value;
    const verif = document.getElementById('verificar');

    if(input === ''){
        alert("Campo invalido! Digite um valor");
    }
    else if(input < 0 ){
        console.log("Numero negativo")
    }
    else {
        console.log("Numero positivo")
    }
}


// EXERCICIO 2
let inputEl = document.getElementById('valorDig');
let resultEl = document.getElementById('resultado');

    function checkNum2() {
        let valorTexto = inputEl.value.trim();

        if (valorTexto === '') {
            resultEl.textContent = 'Por favor, digite um número.';
            return;
        }

        let numero = Number(valorTexto);

        if (Number.isNaN(numero)) {
            resultEl.textContent = 'Valor inválido. Digite um número válido.';
            return;
        }

        let par = '';
        let impar = '';

        if (numero % 2 === 0) {
            par = numero;
            console.log('Par: ' + par);
        } else {
            impar = numero;
            console.log('Ímpar: ' + impar);
        }

        resultEl.innerHTML = 'Par: ' + (par !== '' ? par : '-') + '<br>Ímpar: ' + (impar !== '' ? impar : '-');
    }



// EXERCICIO 3
let buttonEx3 = document.getElementById("verific3");

    function checkNum3(){
        let inputEx3 = document.getElementById("vlEx3").value || '';
        const code = inputEx3.trim();
        const resultEl = document.getElementById('resultado3');

        if(code === '1'){
            resultEl.innerHTML = "Autenticação bem sucedida! <br> Bem-vindo(a), secretária!";
        }
        else if(code === '2'){
            resultEl.innerHTML = "Autenticação bem sucedida! <br> Bem-vindo(a), gerente!";
        }
        else if(code === '3'){
            resultEl.innerHTML = "Autenticação bem sucedida! <br> Bem-vindo(a), diretor!";
        }else{
            resultEl.innerHTML = '';
            alert("Código de acesso inválido. Por favor, tente novamente.");
        }
    }