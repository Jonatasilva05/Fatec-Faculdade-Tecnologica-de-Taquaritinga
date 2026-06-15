document.write("<b>Exercício 3:</b><br>");
fila = []; // Zerando a fila

entrarNaFila("A"); entrarNaFila("B"); entrarNaFila("C"); 
entrarNaFila("D"); entrarNaFila("E"); entrarNaFila("F");

document.write("Tamanho inicial: " + tamanhoDaFila() + "<br>");

sairDaFila(); // Remove A
sairDaFila(); // Remove B
sairDaFila(); // Remove C

document.write("Novo tamanho: " + tamanhoDaFila() + "<br><br>");