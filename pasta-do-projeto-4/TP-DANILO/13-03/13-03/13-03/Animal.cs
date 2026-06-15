using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _13_03
{
    public class Animal
    {
        public string? nome;

        public virtual void EmitirSom()
        {
            Console.WriteLine("Som");
        }
    }
}
