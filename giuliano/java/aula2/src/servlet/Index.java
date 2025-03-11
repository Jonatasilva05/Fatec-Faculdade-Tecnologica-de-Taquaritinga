package servlet;

import java.io.IOException;

import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

public class Index extends HttpServlet {
    
    public void doGet(HttpServletRequest req, HttpServletResponse res) {
        String html = "<!DOCTYPE html>\r\n" + //
                        "<html lang=\"pt-br\">\r\n" + //
                        "<head>\r\n" + //
                        "    <meta charset=\"UTF-8\">\r\n" + //
                        "    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\r\n" + //
                        "    <title>Aula 2 - JAVA</title>\r\n" + //
                        "</head>\r\n" + //
                        "<body>\r\n" + //
                        "\r\n" + //
                        "    <h1>Index</h1>\r\n" + //
                        "    <p>Principal</p>\r\n" + //
                        "    <nav>\r\n" + //
                        "        <a href=\"http://www.fatec.sp.gov.br\" target=\"_blank\">Fatec</a>\r\n" + //
                        "        <a href=\"/curso\">Curso</a>\r\n" + //
                        "    </nav>\r\n" + //
                        "    \r\n" + //
                        "</body>\r\n" + //
                        "</html>";
        try {
            res.getWriter().println(html);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}