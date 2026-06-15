using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _13_03
{
    //Criamos a classe Cachorro e ja aplicamos a herança que vem do elemento pai chamado Animal
    public class Cachorro : Animal
    {
        public override void EmitirSom()
        {
            Console.WriteLine("Au Au!");
        }
    }
}
