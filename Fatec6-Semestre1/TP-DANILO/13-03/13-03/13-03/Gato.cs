using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _13_03
{
    //Criamos a classe Gato e aplicamos a herança do pai que é animal
    public class Gato : Animal
    {
        public override void EmitirSom()
        {
            Console.WriteLine("Miau Miau");
        }
    }
}
