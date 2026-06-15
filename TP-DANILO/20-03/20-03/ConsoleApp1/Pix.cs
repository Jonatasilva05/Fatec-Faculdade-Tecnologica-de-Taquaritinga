using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _20_03
{
    public class Pix : IPagamento
    {
        public void processarPagamento()
        {
            Console.WriteLine("Pagamento realizado em Pix Realizado com Sucessso");
        }
        public void estornarPagamento()
        {
            Console.WriteLine("Estorno realizado no Pix com Sucesso");
        }
    }
}
