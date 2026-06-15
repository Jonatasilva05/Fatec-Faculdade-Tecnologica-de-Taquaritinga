using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _20_03
{
    public class CartaoDebito : Pagamento, IPagamento
    {
        public CartaoDebito(decimal _valorPagamentoDebito, string? _nome) 
        {   
            setValorPagamento(_valorPagamentoDebito);
            nome = _nome;
        }
        public void processarPagamento()
        {
            Console.WriteLine($"Pagamento {nome} com cartão de debito, no valor de {getValorPagamento()} realizado com sucesso");
        }
        public void estornarPagamento()
        {
            Console.WriteLine($"Estorno {nome} cartão de debito, no valor de {getValorPagamento} realizado com sucesso");
        }
    }
}
