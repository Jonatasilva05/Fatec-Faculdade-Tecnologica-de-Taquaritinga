using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _08_05
{
    public class Relatorio : Documento, IImpresso
    {
        public override void processar()
        {
            Console.WriteLine(titulo + "processando....");
        }

        public void imprimir()
        {
            Console.WriteLine(titulo + "gerando relatorio....");
        }
    }
}
