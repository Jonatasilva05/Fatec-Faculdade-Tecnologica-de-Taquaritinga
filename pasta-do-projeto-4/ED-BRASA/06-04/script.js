// var pessoa = [];
// var quantidade = 3;
// for (var i = 0; i < quantidade; i++) {
// var vnome = window.prompt("Digite o nome do empregado " + (i + 1) + ":");
// var vendereco = window.prompt("Digite o endereco do empregado " + (i + 1) + ":");
// var salario = Number(window.prompt("Digite o salário do empregado " + (i + 1) + ":"));
// pessoa.push({
//     nome: vnome,
//     endereco: vendereco,
//     salario: salario
// });
// }
//     document.write("<h3>Lista de Empregados:</h3>");
//     for (var i = 0; i < quantidade; i++) {
//     document.write("Nome: " + pessoa[i].nome + "<br>");
//     document.write("Endereço: " + pessoa[i].endereco + "<br>");
//     document.write("Salário: R$ " + pessoa[i].salario + "<br><br>");
// }



const MAX = 3;
var pessoa = [];
var i,j,aux;
// Grava os elementos no vetor
for ( i = 0; i < MAX; i++) {
    var vnome = window.prompt("Digite o nome do empregado " + (i + 1) + ":");
    var vendereco = window.prompt("Digite o endereco do empregado " + (i + 1) + ":");
    var salario = Number(window.prompt("Digite o salário do empregado " + (i + 1) + ":"));
    pessoa.push({
        nome: vnome,
        endereco: vendereco,
        salario: salario
    });
}
// Lista os elementos do vetor original
document.write("<h3>Lista de Empregados:</h3>");
    for (var i = 0; i < MAX; i++) {
    document.write("Nome: " + pessoa[i].nome + "<br>");
    document.write("Endereço: " + pessoa[i].endereco + "<br>");
    document.write("Salário: R$ " + pessoa[i].salario + "<br><br>");
}

// ordena os elementos do vetor
for(i=0;i<MAX;i++){
    for(j=0;j<MAX-1;j++){
            if (pessoa[j].salario>pessoa[j+1].salario){
            aux = pessoa[j+1].salario
            pessoa[j+1].salario= pessoa[j].salario
            pessoa[j].salario=aux
        }
    }
}
// Lista os elementos do vetor ordenado
    document.write("Valores no vetor ordenado:"+"<br>");
    for (i = 0; i < MAX; i++) {
    document.write("A ordem crescente dos salários é:"+"<br>");
    document.write(`Em ${i+1}° Lugar temos: ${pessoa[i].nome} com salario de  ${pessoa[i].salario}`+'<br>');
}