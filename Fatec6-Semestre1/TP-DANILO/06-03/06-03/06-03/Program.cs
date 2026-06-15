using _06_03;

Corrente contaStefani = new Corrente();
contaStefani.setLimite(500);
Console.WriteLine(contaStefani.getLimite());

//CRIAR UM OBJETO PARA A CONTA POUPANÇA, ATRIBUIR UM VALOR DE 150 REAIS E MOSTRAR ESSE VALOR NA TELA
//ATRIBUA O NOME PARA O TITULAR DA CONTA POUPANÇA E MOSTRE ESSE NOME NA TELA

Poupanca contaJonatas = new Poupanca();
contaJonatas.setSaldo(150);

Conta titularConta = new Conta();
titularConta.titular = "Jonatas";


Console.WriteLine(titularConta.titular);
Console.WriteLine(contaJonatas.getSaldo());