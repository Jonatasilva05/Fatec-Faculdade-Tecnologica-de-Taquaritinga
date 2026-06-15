let itens = [];

//Adiciona elementos no topo
function gravarnaPilha(elemento){
    itens.push(elemento);
}

//Verifica se a pilha está vazia
function estavazia(){
    if(itens.length==0){
        return true;
    }
    else{
        return false
    }
}

//Pilha
//Remove o elemento do topo e mostra quem esta sendo removido

function removerPilha(){
    if(estavazia==true){
        return "pilha vazia"
    }
    else{
        itens.pop()
    }
}

//Retorna o Topo sem remover
function topo(){
    if(estavazia()==true){
        return "pilha vazia"
    }
    else{
        return itens[itens.length-1]    
    }
}

function tamanho(){
    return itens.length
}
function imprimir(){
    document.write(itens.join(" <- "))
}

//Teste principal
gravarnaPilha("a")
gravarnaPilha("b")
gravarnaPilha("c")
imprimir()
document.write("<br>")

//mostrar topo

document.write("o topo é " + topo())
//Remover da pilha

document.write("<br>")
document.write(removerPilha())
document.write("<br>")
imprimir()  