package app.dao;

import java.sql.Connection;
import java.sql.PreparedStatement;

import app.model.Livro;
import app.singleton.Conexao;

public class LivroDao {
    private Connection con;

    public LivroDao() {
        this.con = Conexao.getInstancia().getConexao();
    }

    public String salvar(Livro livro) {
        String sql = " INSERT INTO livro (titulo, editora, ano) VALUES (?, ?, ?); ";
        PreparedStatement ps = this.con.prepareStatement(sql);
    }
}