package app.singleton;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class Conexao {
    private static Conexao instancia;
    private Connection connection;
    private String driver = "com.mysql.jdbc.Driver";
    private String url = "jdbc:mysql://localhost/ds2_livro";
    private String usuario = "root";
    private String senha = "";

    public Connection getConexao() {
        try {
            Class.forName(driver);
            connection = DriverManager.getConnection(url, usuario, senha);
        } catch (ClassNotFoundException | SQLException e) {
            e.printStackTrace();
        }
        return connection;
    }

    public synchronized static Conexao getInstancia() {
        if (instancia == null) {
            instancia = new Conexao();
        }
        return instancia;
    }
}
