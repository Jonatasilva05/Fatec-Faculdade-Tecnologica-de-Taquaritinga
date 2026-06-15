package app;

import java.awt.Dimension;

import javax.swing.JFrame;
import javax.swing.JLabel;

import org.eclipse.jetty.server.Server;
import org.eclipse.jetty.server.ServerConnector;
import org.eclipse.jetty.servlet.ServletContextHandler;

public class Servidor {
	
	public static void main(String[] args) {
		// Interface grafica do servidor
		JFrame frame = new JFrame();	
		frame.setTitle("Jetty");
		frame.setPreferredSize(new Dimension(180, 180));
		frame.setLayout(null);
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frame.pack();
		frame.setLocationRelativeTo(null);
		
		JLabel label = new JLabel();
		label.setText("Servidor Jetty Iniciado!");
		label.setBounds(15, 15, 160, 100);
		frame.add(label);
		
		frame.setVisible(true);
		
		// Inicializacao do servidor Jetty
		try {
			Server server = new Server();
			ServerConnector c = new ServerConnector(server);
			c.setName("Servlet");
			c.setHost("0.0.0.0");	
			c.setPort(9000);		
			
			ServletContextHandler handler = new ServletContextHandler(server, "/", false, false);			//
			
			// Adicionar Servlets
			// handler.addServlet(Arquivo.class, "/");
			// Servlets
			//handler.addServlet(Exemplo.class, "/");
			
			server.addConnector(c);
			server.start();
			
			System.out.println("Servidor Jetty iniciado!");
		} catch (Exception e) {
			e.printStackTrace();
		} 		
	}	
}
