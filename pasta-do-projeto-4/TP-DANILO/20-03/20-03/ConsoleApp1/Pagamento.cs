using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _20_03
{
    public class Pagamento
    {
        private decimal valorPagamento;
        public void setValorPagamento(decimal _valorPagamento)
        {
            valorPagamento = _valorPagamento;
        }
        public decimal getValorPagamento()
        {
            return valorPagamento;
        }

        public string? nome;
    }
}
