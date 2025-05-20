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
        if(pet.getCodigo() > 0) {
            sql = " UPDATE pet SET nome = ?, valor = ?, telefone = ?, nomepet = ? "+
                  " WHERE codigo = ? ";
        } else {
            sql = " INSERT INTO pet (nome, valor, telefone, nomepet) "+
                     " VALUES (?, ?, ?, ?); ";
        }
        try {
            PreparedStatement ps = this.con.prepareStatement(sql);
            ps.setString(1, pet.getNome());
            ps.setDouble(2, pet.getValor());
            ps.setString(3, pet.getTelefone());
            if (pet.getCodigo() > 0) {
                ps.setString(4, pet.getNomepet());
            }
            ps.execute();
            ps.close();
            return "pet salvo!";
        } catch (SQLException e) {
            e.printStackTrace();
            return "Houve um erro! Tente novamente!";
        }
    }

    public List<Pet> listar() {
        List<Pet> petPet = new ArrayList<>();
        String sql = " SELECT * FROM pet ";
        try {
            PreparedStatement ps = this.con.prepareStatement(sql);
            ResultSet rs = ps.executeQuery();
            while (rs.next()) {
                Pet pet = new Pet();
                pet.setCodigo(rs.getInt("codigo"));
                pet.setNome(rs.getString("nome"));
                pet.setValor(rs.getDouble("valor"));
                pet.setTelefone(rs.getString("telefone"));
                pet.setNomepet(rs.getString("nomepet"));
                petPets.add(pet);
            }
            ps.close();
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return petPets;
    }

    public Pet gPet(int codigo) {
        Pet pet = new Pet();
        String sql = " SELECT * FROM livro WHERE codigo = ? ";
        try {
            PreparedStatement ps = this.con.prepareStatement(sql);
            ps.setInt(1, codigo);
            ResultSet rs = ps.executeQuery();
            rs.next();
            pet.setCodigo(rs.getInt("codigo"));
            pet.setTitulo(rs.getString("titulo"));
            pet.setEditora(rs.getString("editora"));
            pet.setAno(rs.getInt("ano"));
            ps.close();

        } catch (SQLException e) {
            e.printStackTrace();
        }
        return pet;
    }
    
    public List<Pet> getLivroPorTitulo(String titulo) {
        List<Pet> petPets = new ArrayList<>();
        String sql = " SELECT * FROM pet WHERE titulo LIKE ? ";
        try {
            PreparedStatement ps = this.con.prepareStatement(sql);
            ps.setString(1, "%" + titulo + "%");
            ResultSet rs = ps.executeQuery();
            while (rs.next()) {
                Pet pet = new Pet();
                pet.setCodigo(rs.getInt("codigo"));
                pet.setTitulo(rs.getString("titulo"));
                pet.setEditora(rs.getString("editora"));
                pet.setAno(rs.getInt("ano"));
                petPets.add(pet);
            }
            ps.close();
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return petPets;
    }
}