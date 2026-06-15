using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _20_03
{
    public class CartaoCredito : Pagamento, IPagamento
    {
        public CartaoCredito(decimal _valorPagamento, string _nome) 
        {
            setValorPagamento(_valorPagamento);
            nome = _nome;
        }
        public void processarPagamento()
        {
            Console.WriteLine($"Pagamento {nome} Relizado com Cartão de Crédito, no valor de {getValorPagamento()} realizado com sucesso");
        }
        public void estornarPagamento()
        {
            Console.WriteLine($"Estorno {nome} ao Cartão de Credito, no valor de {getValorPagamento()} realizado com sucesso");
        }
    }
}
