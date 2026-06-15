using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _08_05
{
    public class Contrato : Documento, IImpresso
    {
        public Contrato(string _titulo)
        {
            titulo = _titulo;
        }
        public override void processar()
        {
            Console.WriteLine(titulo + "processando....");
        }

        public void imprimir()
        {
            Console.WriteLine(titulo + "sendo impresso....");
        }
    }
}
