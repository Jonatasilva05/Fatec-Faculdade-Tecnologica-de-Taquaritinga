using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _24_04
{
    public class Professor : Pessoa
    {
        public override void boasVindas()
        {
            Console.WriteLine("Bem vindo professor");
        }
        public void cadastrarProfessor()
        {
            Console.WriteLine("Professor cadastrado");
        }
    }
}
