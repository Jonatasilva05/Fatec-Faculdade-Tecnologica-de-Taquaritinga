const max = 6;
let v = [];
let i, valor, encontrou;

// Grava no Vetor ou Arrays
for(i = 0; i < max; i++){
    valor = Number(window.prompt("Digite Numero"));
    v.push(valor);
}
// Lista os elementos no vetor
document.write("<br>"); // Corrigido: 'document' minúsculo e adicionado <>

for(i = 0; i < max; i++){
    document.write(`${i}: ${v[i]}` + '<br>');
}

// Verifica se o valor 7 existe no vetor ou arrays
document.write("<br>");
encontrou = false; // Corrigido: sintaxe de atribuição e 'false' minúsculo

for(i = 0; i < max; i++){
    if(v[i] === 7){ // Recomendado usar === para comparação
        encontrou = true; // Corrigido: 'true' minúsculo
        document.write(`O valor 7 foi encontrado na posição ${i}` + '<br>');
    }
}

if(!encontrou){
    document.write("O valor 7 não foi encontrado");
}
