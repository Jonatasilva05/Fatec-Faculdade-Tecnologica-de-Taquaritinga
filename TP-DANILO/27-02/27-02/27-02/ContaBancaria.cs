using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _27_02
{
    internal class ContaBancaria
    {
        private double saldo;


        //METODO PARA LIBERAR O ACESSO DO OBEJTO A NOSSA CLASSE PRIVADA
        //ATRIBUIR VALOR
        public void setSaldo(double _saldo)
        {
            saldo = _saldo;
        }

        //LER O VALOR
        public double getSaldo()
        {
            return saldo;
        }


        private double limiteConta;

        public void setLimiteConta(double _limiteConta)
        {
            limiteConta = _limiteConta;
        }

        public double getLimiteConta()
        {
            return limiteConta;
        }


        public string? titular;
        public int numeroConta;
        public string? perfil;


        //CONSTRUTOR PADRÃO
        public ContaBancaria()
        {
        }


        //CONSTRUTOR 2
        public ContaBancaria(double _saldo)
        {
            saldo = _saldo;
        }


        //CONSTRUTOR 3
        public ContaBancaria(string _titular, int _numeroConta)
        {
            titular = _titular;
            numeroConta = _numeroConta;
        }

        //CONTRUTOR 4 
        public ContaBancaria(string _perfil)
        { 
            perfil = _perfil;
        }
    }
}
