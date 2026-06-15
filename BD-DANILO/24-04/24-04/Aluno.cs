using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _24_04
{
    public class Aluno : Pessoa
    {
        public override void boasVindas()
        {
            Console.WriteLine("Bem vindo Aluno");
        }

        //abstract serve so apra criar uma classe generica - consegue ultilizar ela como herança para classes mais especificas
        public void cadastrarAluno()
        {
            Console.WriteLine("Aluno cadastrado");
        }
    }
}
