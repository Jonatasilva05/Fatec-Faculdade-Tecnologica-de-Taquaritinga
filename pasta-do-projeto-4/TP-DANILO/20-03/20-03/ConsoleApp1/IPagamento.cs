using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _20_03
{
    public interface IPagamento
    {
        public void processarPagamento();

        public void estornarPagamento();
    }
}
