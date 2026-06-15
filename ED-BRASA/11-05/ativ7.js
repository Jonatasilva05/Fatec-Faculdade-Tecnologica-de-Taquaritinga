document.write("<b>Exercício 7:</b><br>");
fila = []; // Zerando a fila

entrarNaFila("Doc1");
entrarNaFila("Doc2");
entrarNaFila("Doc3");
entrarNaFila("Doc4");
entrarNaFila("Doc5");

// Salvamos o documento removido em uma variável para poder mostrá-lo
let documentoImpresso = sairDaFila(); 

document.write("Documento impresso: " + documentoImpresso + "<br>");
document.write("Fila restante: " + imprimirFila() + "<br><br>");