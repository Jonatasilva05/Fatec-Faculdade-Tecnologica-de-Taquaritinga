using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _20_03
{
    public class Cash : Pagamento, IPagamento
    {
        public Cash(decimal _valorPagamentoCash, string? _nome) 
        {
            setValorPagamento(_valorPagamentoCash);
            nome = _nome;
        }
        public void processarPagamento()
        {
            Console.WriteLine($"Pagamento {nome} em cash, no valor de {getValorPagamento()} realizado com sucesso");
        }
        public void estornarPagamento()
        {
            Console.WriteLine($"Estorno {nome} em cash, no valor de {getValorPagamento()} realizado com sucesso");
        }
    }
}
