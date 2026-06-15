document.write("<b>Exercício 1:</b><br>");
fila = []; // Zerando a fila

entrarNaFila(1);
entrarNaFila(2);
entrarNaFila(3);
entrarNaFila(4);
entrarNaFila(5);

sairDaFila(); // Remove o 1
sairDaFila(); // Remove o 2

document.write("Estado da fila: " + imprimirFila() + "<br><br>");