// //EXERCICIO 1.
// const max = 5;
// let v = [];
// let i, valor, encontrou;

//     // Grava no Vetor ou Arrays
//     for(i = 0; i < max; i++){
//         valor = Number(window.prompt("Digite Numero"));
//         v.push(valor);
//     }

//     // Verifica se o valor 0 existe no vetor ou arrays
//     document.write("<br>");
//     encontrou = false;

//     for(i = 0; i < max; i++){
//         if(v[i] === 0){
//             encontrou = true;
//             document.write(`O valor 0 foi encontrado na posição ${i}` + '<br>');
//         }
//     }

//     if(!encontrou){
//         document.write("O valor 0 não foi encontrado");
//     }





// //EXERCICIO 2.
// const max = 20;
// let v = [];
// let i, valor, encontrou;

//     // Grava no Vetor ou Arrays
//     for(i = 0; i < max; i++){
//         valor = Number(window.prompt("Digite Numero"));
//         v.push(valor);
//     }
//     // Lista os elementos no vetor
//     document.write("<br>");

//     for(i = 0; i < max; i++){
//         document.write(`${i}: ${v[i]}` + '<br>');
//     }

//     // Faz a verificação se o valor 0 existe no vetor ou arrays
//     document.write("<br>");
//     encontrou = false;

//     for(i = 0; i < max; i++){
//         if(v[i] === 3){ 
//             encontrou = true;
//             document.write(`O valor 3 foi encontrado na posição ${i}` + '<br>');
//         }
//     }

//     if(!encontrou){
//         document.write("O valor 3 não foi encontrado");
//     }




    
// //EXERCICIO 3.    
// const max = 5;
// let v = [];
// let i, valor;

//     // Grava no Vetor ou Arrays
//     for (i = 0; i < max; i++) {
//         valor = Number(window.prompt(`Digite o número para a posição ${i}:`));
        
//         // Aqui ele vai "comparar" para ver se o valor é negativo e se for, atribui 0
//         if (valor < 0) {
//             v.push(0);
//         } else {
//             v.push(valor);
//         }
//     }

//     // Lista os elementos no vetor
//     document.write("<strong>Resultado do Vetor (Negativos viram 0):</strong><br>");

//     for (i = 0; i < max; i++) {
//         document.write(`Posição ${i}: ${v[i]}<br>`);
//     }





// //EXERCICO 4.
// const max = 5;
// let v = [];
// let i, valor, encontrou;

//     // Grava no Vetor ou Arrays
//     for(i = 0; i < max; i++){
//         valor = Number(window.prompt("Digite Numero"));
//         v.push(valor);
//     }
//     // Lista os elementos no vetor
//     document.write("<br>");

//     for(i = 0; i < max; i++){
//         document.write(`${i}: ${v[i]}` + '<br>');
//     }

//     document.write("<br>")
//     document.write("<strong>Valores acima de 10:</strong><br>");
//     document.write("<br>")  

//     //TEMOS QUE DECLARAR A VARIAVEL FALSA PORQUE SE ELA SE TORNAR VERDADEIRA TERA QUE SE 10 OU MAIOR QUE 10
//     let maiorDez = false;

//     for(i = 0; i < max; i++){
//         //FARA A VERIFICAÇÃO SE OS VALORES SÃO MAIORES QUE 10
//         if(v[i] >= 10){ 
//             document.write(`Posição ${i}: ${v[i]}<br>`);
//             maiorDez = true;
//         }
//     }

//     if(!algumMaior){
//         document.write("Nenhum número maior que 10 foi encontrado.");
//     }





// const max = 5;
// let v = [];
// let i, valor;

//     //Grava no Vetor ou Arrays
//     for(i = 0; i < max; i++){
//         valor = Number(window.prompt("Digite Numero"));
//         v.push(valor);
//     }

//     //Aqui vai mostra o vetor *ANTES* da substituição
//     document.write("<strong>Vetor Original:</strong><br>");
//     for(i = 0; i < max; i++){
//         document.write(`Posição ${i}: ${v[i]}<br>`);
//     }

//     //Substitui os valores pares por 0
//     for(i = 0; i < max; i++){
//         if(v[i] % 2 === 0){
//             v[i] = 0;
//         }
//     }

//     document.write("<br>");

//     //Mostra o vetor *DEPOIS* da substituição
//     document.write("<strong>Vetor Após Substituir Pares por 0:</strong><br>");
//     for(i = 0; i < max; i++){
//         document.write(`Posição ${i}: ${v[i]}<br>`);
//     }