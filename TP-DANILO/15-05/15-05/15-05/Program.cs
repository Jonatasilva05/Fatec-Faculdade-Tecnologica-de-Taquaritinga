using _15_05.Models;
using _15_05.Repository;

AlunoRepository repo = new AlunoRepository();

// CRIANDO UM OBJETO PARA ALUNO
Aluno alunoNovo = new Aluno();

Console.WriteLine("Digite o Nome do Aluno: ");
alunoNovo.nome = Console.ReadLine();

Console.WriteLine("Digite a Idade do Aluno: ");
alunoNovo.idade = int.Parse(Console.ReadLine());

Console.WriteLine("Digite o Email do Aluno: ");
alunoNovo.email = Console.ReadLine();

repo.inserir(alunoNovo);
