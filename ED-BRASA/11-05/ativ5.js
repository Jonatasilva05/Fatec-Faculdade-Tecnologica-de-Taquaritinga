document.write("<b>Exercício 5:</b><br>");
fila = []; // Zerando a fila

entrarNaFila("Cliente 1");
entrarNaFila("Cliente 2");
entrarNaFila("Cliente 3");
entrarNaFila("Cliente 4");
entrarNaFila("Cliente 5");

sairDaFila(); // Cliente 1 atendido
sairDaFila(); // Cliente 2 atendido

document.write("Ainda aguardam: " + imprimirFila() + "<br><br>");