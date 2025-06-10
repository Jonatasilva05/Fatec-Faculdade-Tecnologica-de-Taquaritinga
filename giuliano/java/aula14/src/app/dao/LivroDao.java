package app.dao;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

import app.model.Livro;
import app.singleton.Conexao;

public class LivroDao {
    private Connection con;

    public LivroDao() {
        this.con = Conexao.getInstancia().getConexao();
    }

    public String salvar(Livro livro) {
        String sql = "";
        if (livro.getCodigo() > 0 ) {
            sql = " UPDATE livro SET titulo = ?, editora = ?, ano = ?" +
                  " WHERE codigo = ?"; 
        } else { 
            sql = " INSERT INTO livro (titulo, editora, ano) " +
                " VALUES (?, ?, ?); "; 
        }
        try {
            PreparedStatement ps = this.con.prepareStatement(sql);
            ps.setString(1, livro.getTitulo());
            ps.setString(2, livro.getEditora());
            ps.setInt(3, livro.getAno());
            if(livro.getCodigo() > 0) {
                ps.setInt(4, livro.getCodigo());
            }
            ps.execute();
            ps.close();
            return "Livro salvo!";
        } catch (SQLException e) {
            e.printStackTrace();
            return "Houve um erro! Tente novamente!";
        }
    }

    public List<Livro> listar() {
        List<Livro> listaLivros = new ArrayList<>();
        String sql = " SELECT * FROM livro ";
        try {
            PreparedStatement ps = this.con.prepareStatement(sql);
            ResultSet rs = ps.executeQuery();
            while (rs.next()) {
                Livro livro = new Livro();
                livro.setCodigo(rs.getInt("codigo"));
                livro.setTitulo(rs.getString("titulo"));
                livro.setEditora(rs.getString("editora"));
                livro.setAno(rs.getInt("ano"));
                listaLivros.add(livro);
            }
            ps.close();

        } catch (SQLException e) {
            e.printStackTrace();
        }
        return listaLivros;
    }

    public Livro getLivroPorCodigo(int codigo) {
        Livro livro = new Livro();
        String sql = "SELECT * FROM livro WHERE codigo = ?";
        try {
            PreparedStatement ps = this.con.prepareStatement(sql);
            ps.setInt(1, codigo);
            ResultSet rs = ps.executeQuery();
            rs.next();
            livro.setCodigo(rs.getInt("codigo"));
            livro.setTitulo(rs.getString("titulo"));
            livro.setEditora(rs.getString("editora"));
            livro.setAno(rs.getInt("ano"));
            ps.close();
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return livro;
    }

    public List<Livro> getLivroPorTitulo(String titulo) {
        List<Livro> listaLivros = new ArrayList<>();
        String sql = "SELECT * FROM livro WHERE titulo LIKE ?";
        try {
            PreparedStatement ps = this.con.prepareStatement(sql);
            ps.setString(1, "%" + titulo + "%");
            ResultSet rs = ps.executeQuery();
            while (rs.next()) {
                Livro livro = new Livro();
                livro.setCodigo(rs.getInt("codigo"));
                livro.setTitulo(rs.getString("titulo"));
                livro.setEditora(rs.getString("editora"));
                livro.setAno(rs.getInt("ano"));
                listaLivros.add(livro);
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return listaLivros;
    }

    public String excluir(int codigo) {
        String sql = " DELETE FROM livro WHERE codigo = ? ";
        try {
            PreparedStatement ps = this.con.prepareStatement(sql);
            ps.setInt(1, codigo);
            ps.execute();
            ps.close();
            return "Livro excluido!";
        } catch (SQLException e) {
            e.printStackTrace();
            return "Houve um erro, Tente novamente!";
        }
    }
}
