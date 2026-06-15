using _13_02;

Carro meuCarro = new Carro();

Console.WriteLine("---------Informações do Carro---------");

Console.WriteLine("Informe a Marca do Carro");
meuCarro.marca = Console.ReadLine();

Console.WriteLine("Informe a Modelo do Carro");
meuCarro.modelo = Console.ReadLine();

Console.WriteLine("Informe a Ano do Carro");
meuCarro.ano = int.Parse(Console.ReadLine());

Console.WriteLine("Informe a Placa do Carro");
meuCarro.placa = Console.ReadLine();





Console.WriteLine("------------------");





meuCarro.MostrarInfoCarro();

meuCarro.ligarCarro();
meuCarro.acelerar();
meuCarro.brecar();
meuCarro.desligarCarro();

Console.WriteLine("----------Carro Antigo--------");

Carro CarroAntigo = new Carro();

Console.WriteLine("Informe a Marca do Carro");
CarroAntigo.marca = Console.ReadLine();

Console.WriteLine("Informe a Modelo do Carro");
CarroAntigo.modelo = Console.ReadLine();

Console.WriteLine("Informe a Ano do Carro");
CarroAntigo.ano = int.Parse(Console.ReadLine());

Console.WriteLine("Informe a Placa do Carro");
CarroAntigo.placa = Console.ReadLine();

CarroAntigo.ligarCarro();
CarroAntigo.acelerar();
CarroAntigo.brecar();
CarroAntigo.desligarCarro();    