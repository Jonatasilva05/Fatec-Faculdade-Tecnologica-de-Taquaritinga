//// QUESTÃO 1
// const max = 10
//     let v = []
//     let i, j, aux, valor

//     //grava os elementos
//     for(i=0; i<max; i++){
//         valor = Number(window.prompt("Digite o valor"))
//         v.push(valor)
//     }

//     for(i=0; i<max; i++){
//         for(j=0; j<max-1; j++){
//             if(v[j] < v[j+1]){
//                 aux = v[j+1]
//                 v[j+1] = v[j]
//                 v[j] = aux
//             }
//         }
//     }
//     for(i=0; i<max; i++){
//         document.write(i + " " + v[i] + "<br>")
//     }



//// QUESTÃO 2
const max = 5
    let v = []
    let i, j, aux, valor

    //grava os elementos
    for(i=0; i<max; i++){
        valor = Number(window.prompt("Digite o valor"))
        v.push(valor)
    }

    for (i = 0; i < max; i++) {
        for(j=0;j<max-1;j++){
        if(v[i] > v[j]) {
            aux = v[j+1]
            v[j+1] = v[j]
            v[j] = aux           
        }
    }
}

document.write("O maior valor é: " + v[max-1] + " e está na posição: " + (max-1) + "<br>" + "E o numero menor é: " + v[0] + " e está na posição: " + 0);