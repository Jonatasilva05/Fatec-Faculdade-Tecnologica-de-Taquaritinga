# PROGRAMAÇÃO ORIENTADA A OBJETO (Paradigma)

## Classe
Com a classe conseguimos gerar qualquer tipo de objeto
- Caracteristicas *(Propriedades)* -> R.A, IDADE, NOME
- Ações *(Métodos)* -> ESTAGIAR, FREQUENTAR AULA, FAZER PROVA

## Objeto
- Aluno SI
- Aluno ADS
- Aluno PI

---

# Exemplo de C#
    Public Class Aluno 
    {
        public int RA;

        public Aluno(string _nome)
        {
            nome = _nome;
        }


        public String Nome;
        public Int Idade;

        public void Estagiar()
        {
            Console.WriteLine("Estagiando!");
        }

        Aluno AlunoSI = New Aluno();

        AlunoSI.RA = 20345;
        AlunoSI.Nome = "Danilo";
        AlunoSI.Estagiar();

        Aluno AlunoADS = new AlunoAds("Pedro");
    }

Public Class Aluno 
{

    public int RA;


    public String Nome;
    public Int Idade;

    public void Estagiar()
    {
        Console.WriteLine("Estagiando!");
    }
}

*Modificadores de Acesso*
- Public  - Acesso em todo o projeto
- Private - Acesso somente dentro da classe
- Internal
- Protected

---

## Construtor 2
    Public Aluno (Int_RA, String_Nome)
    {
        RA = _RA;
        Nome = _Nome;
    }

        Aluno AlunoPI = New Aluno(20, "José");

    Public Aluno()
    {

    }

---

    Public Class Aluno
    {
        Private Int RA; //ENCAPSULAMENTO

        //METODO PARA ATRIBUIÇÃO DE VALOR
        Public Void SetRA(Int _RA)
        {
            RA = _RA
        }

        Public void GetRA(Int _RA)
        {
            Console.WriteLine(RA _RA);
        }

        Public String Nome;
        Public String Email;
        Public String Idade;
    }

---

<br>

---

## Conceito de Herança

Classe Pai **ALUNO** -> RA, IDADE, NOME, FREQUENTAR_AULA

CLasse Filhas **ALUNO CALOURO** FREQUENCIA_OBRIGATORIA

CLasse Filhas **ALUNO VETERANO** TCC, ESTAGIAR 

"SubClasse" do ALUNO VETERANO **ALUNO 2 BIMESTRE** PI 2

"SubClasse" do ALUNO VETERANO **ALUNO 3 BIMESTRE** PI 3

---
<br>

Classe Pai **VEICULO**

Classe Filho **TERRESTRE**

Classe Filho **AÉREO**

Classe Filho **MARÍTIMO**

---
<br>

Classe Pai **ANIMAL**

Classe Filho **VERTEBRADO**

"SubClasse" do VERTEBRADO **MAMIFERO**

"SubClasse" do VERTEBRADO **AVE**

Classe Filho **INVERTEBRADO**

---
<br>