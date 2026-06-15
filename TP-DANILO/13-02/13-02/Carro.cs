using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _13_02
{
    public class Carro
    {
        //Caracteristicas do Carro = Propriedades/Atributos
        // A ? (interrogação é porque ele pode ser umm valor nulo)
        public string? marca; 
        public string? modelo;
        public int ano;
        public string? placa;

        
        //Ações do Carro - Metodos/Comportamentos
        public void MostrarInfoCarro()
        {
            Console.WriteLine("Marca: "  + marca);
            Console.WriteLine("Modelo: " + modelo);
            Console.WriteLine("Ano: " + ano); 
            Console.WriteLine("Placa: " + placa);
        }

        //void e para indicar que é um metodo
        public void acelerar()
        {
            Console.WriteLine("O carro acelerou");
        }

        public void brecar()
        {
            Console.WriteLine("O carro freou");
        }

        public void ligarCarro()
        {
            Console.WriteLine("O carro Ligou");
        }

        public void desligarCarro()
        {
            Console.WriteLine("O carro Desligou");

        }
    }
}
