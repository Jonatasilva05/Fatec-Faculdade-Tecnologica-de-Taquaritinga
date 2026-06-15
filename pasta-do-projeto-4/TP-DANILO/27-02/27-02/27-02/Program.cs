using _27_02;

//CRIANDO O OBJETO ULTILIZANDO O CONSTRUTOR PADRÃO
ContaBancaria contaBancaria1 = new ContaBancaria();
contaBancaria1.setSaldo(800);
Console.WriteLine("O valor da sua conta é: " + contaBancaria1.getSaldo());


//CRIANDO O OBJETO ULTILIZANDO O CONTRUTOR 2
ContaBancaria contaBancaria2 = new ContaBancaria(500);


//CRIANDO O OBJETO ULTILIZANDO O CONTRUTOR 3
ContaBancaria contaBancaria3 = new ContaBancaria("Maicon", 12589702);


//CRIANDO O OBJETO ULTILIZANDO O CONTRUTOR 4
ContaBancaria contaBancaria4 = new ContaBancaria(1000.50);


//CRIANDO O OBJETO ULTILIZANDO O CONTRUTOR 5
ContaBancaria contaBancaria5 = new ContaBancaria("basico");



ContaBancaria contaBancaria6 = new ContaBancaria();
contaBancaria6.setLimiteConta(1500);
Console.WriteLine("O Limite da sua conta é: " + contaBancaria6.getLimiteConta());