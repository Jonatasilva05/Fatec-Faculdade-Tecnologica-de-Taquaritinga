const max = 5
    let v = []
    let i, j, aux, valor

    //grava os elementos
    for(i=0; i<max; i++){
        valor = Number(window.prompt("Digite o valor"))
        v.push(valor)
    }

    //lista o array original
    // for(i=0; i<max; i++){
    //     document.write(i + " " + v[i] + "<br>")
    // };

    for(i=0; i<max; i++){
        for(j=0; j<max-1; j++){
            if(v[j] > v[j+1]){
                aux = v[j+1]
                v[j+1] = v[j]
                v[j] = aux
            }
        }
    }
    for(i=0; i<max; i++){
        document.write(i + " " + v[i] + "<br>")
    }