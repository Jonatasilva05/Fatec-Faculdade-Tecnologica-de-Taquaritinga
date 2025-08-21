package app.dao;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

import app.model.Pet;
import app.singleton.Conexao;

public class PetDao {
    private Connection con;

    public PetDao() {
        this.con = Conexao.getInstancia().getConexao();
    }

    public String salvar(Pet pet) {
        String sql = "";
        if (pet.getCodigo() > 0 ) {
            sql = " UPDATE pet SET nome = ?, tutor = ?, raca = ?, celular = ?" +
                  " WHERE codigo = ?"; 
        } else { 
            sql = " INSERT INTO pet (nome, tutor, raca, celular) " +
                " VALUES (?, ?, ?, ?); "; 
        }
        try {
            PreparedStatement ps = this.con.prepareStatement(sql);
            ps.setString(1, pet.getNome());
            ps.setString(2, pet.getTutor());
            ps.setString(3, pet.getRaca());
            ps.setString(4, pet.getCelular());

            if(pet.getCodigo() > 0) {
                ps.setInt(4, pet.getCodigo());
            }
            ps.execute();
            ps.close();
            return "Pet Cadastrado!";
        } catch (SQLException e) {
            e.printStackTrace();
            return "Houve um erro! Tente novamente!";
        }
    }

    public List<Pet> listar() {
        List<Pet> listaPet = new ArrayList<>();
        String sql = " SELECT * FROM pet ";
        try {
            PreparedStatement ps = this.con.prepareStatement(sql);
            ResultSet rs = ps.executeQuery();
            while (rs.next()) {
                Pet pet = new Pet();
                pet.setCodigo(rs.getInt("codigo"));
                pet.setNome(rs.getString("nome"));
                pet.setTutor(rs.getString("tutor"));
                pet.setRaca(rs.getString("raca"));
                pet.setCelular(rs.getString("celular"));
                listaPet.add(pet);
            }
            ps.close();

        } catch (SQLException e) {
            e.printStackTrace();
        }
        return listaPet;
    }

    public Pet getLivroPorCodigo(int codigo) {
        Pet livro = new Pet();
        String sql = "SELECT * FROM pet WHERE codigo = ?";
        try {
            PreparedStatement ps = this.con.prepareStatement(sql);
            ps.setInt(1, codigo);
            ResultSet rs = ps.executeQuery();
            rs.next();
            Pet pet = new Pet();
            pet.setCodigo(rs.getInt("codigo"));
            pet.setNome(rs.getString("nome"));
            pet.setTutor(rs.getString("tutor"));
            pet.setRaca(rs.getString("raca"));
            pet.setCelular(rs.getString("celular"));
            ps.close();
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return livro;
    }

    public List<Pet> getPetnome(String titulo) {
        List<Pet> listapet = new ArrayList<>();
        String sql = "SELECT * FROM pet WHERE titulo LIKE ?";
        try {
            PreparedStatement ps = this.con.prepareStatement(sql);
            ps.setString(1, "%" + titulo + "%");
            ResultSet rs = ps.executeQuery();
            while (rs.next()) {
                Pet pet = new Pet();
                pet.setCodigo(rs.getInt("codigo"));
                pet.setNome(rs.getString("nome"));
                pet.setTutor(rs.getString("tutor"));
                pet.setRaca(rs.getString("raca"));
                pet.setCelular(rs.getString("celular"));
                listapet.add(pet);
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return listapet;
    }
}
