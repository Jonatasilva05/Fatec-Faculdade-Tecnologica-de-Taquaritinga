using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _06_03
{
    public class Poupanca : Conta
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
    }
}
