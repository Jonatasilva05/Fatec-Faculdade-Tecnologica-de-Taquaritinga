using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _08_05
{
    public abstract class Documento
    {
        public string? titulo;

        //METODO CONCRETO
        public void exibirTitulo()
        {
            //Console.WriteLine($"O titulo é {titulo} ");
            Console.WriteLine("O titulo é: " + titulo);
        }

        //METODO ABSTRATO
        public abstract void processar();
    }
}
