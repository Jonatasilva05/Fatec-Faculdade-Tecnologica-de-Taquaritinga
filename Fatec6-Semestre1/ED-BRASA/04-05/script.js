let itens = [];

function gravarnafila(elemento) {
    itens.push(elemento);
}

function estavazia() {
 if (itens.length == 0){
    return true;
  }
  else {    
    return false;
  }
}      

function inicio() {
    if (estavazia()){
        return "Fila vazia";
    }
    else {
        return itens[0];
    }
}

function tamanhofila() {
    return itens.length;
}

function removedafila() {
    if (estavazia()){
        return "Fila vazia";
    }
    else {
        return itens.shift();
    }
}

function imprimir() {
    document.write(itens.join("<-"));
}

gravarnafila("A");
gravarnafila("B");
gravarnafila("C");
imprimir();
document.write("<br>");
document.write(removedafila());
document.write("<br>");
imprimir();