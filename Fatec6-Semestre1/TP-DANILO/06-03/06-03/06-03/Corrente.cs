using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _06_03
{
    public class Corrente : Conta
    // Quando usamos o caractere ":" ele esta indicando que, Corrente que esta herdando de Conta, ou seja, Corrente é um tipo de Conta
    {
        private decimal saldo;
        public void setSaldo(decimal _saldo)
        {
            saldo = _saldo;
        }

        public decimal getSaldo()
        {
            return saldo;
        }


        private decimal limite;
        public void setLimite(decimal _limite)
        {
            limite = _limite;
        }

        public decimal getLimite()
        { 
            return limite;
        }
    }
}
