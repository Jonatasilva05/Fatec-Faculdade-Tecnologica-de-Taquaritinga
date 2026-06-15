using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Microsoft.Data.SqlClient;
using _15_05.Models;

namespace _15_05.Repository
{
    public class AlunoRepository
    {
        string conexao = "Server=192.168.0.39;Database=BD_FACULDADE_JONATAS;User Id=aluno;Password=Aluno@123;Encrypt=False;TrustServerCertificate=True;";

        public void inserir(Aluno alunoNovo)
        {
            using (SqlConnection conn = new SqlConnection(conexao))
            {
                string query = "INSERT INTO ALUNO (NOME, IDADE, EMAIL) VALUES (@NOME, @IDADE, @EMAIL);";
                SqlCommand cmd = new SqlCommand(query, conn);

                cmd.Parameters.AddWithValue("@NOME", alunoNovo.nome);
                cmd.Parameters.AddWithValue("@IDADE", alunoNovo.idade);
                cmd.Parameters.AddWithValue("@EMAIL", alunoNovo.email);

                conn.Open();
                cmd.ExecuteNonQuery();
                Console.WriteLine("Aluno Inserido com Sucesso");
            }
        }
    }
}
