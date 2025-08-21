package app.controller;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PostMapping;

import app.dao.LivroDao;
import app.model.Livro;
import jakarta.servlet.http.HttpServletRequest;

@Controller
public class LivroController {
    
    @GetMapping("/cadastrar")
    public String cadastrar() {
        return "cadastrarlivro";
    } 

    @PostMapping("/cadastrar")
    public String cadastrarLivro(@ModelAttribute(name="livro") Livro livro, 
        Model model) {
        LivroDao dao = new LivroDao();
        model.addAttribute("mensagem", dao.salvar(livro));
        return "mensagem";
    }

    @GetMapping("/listar")
    public String listar(Model model) {
        LivroDao dao = new LivroDao();
        model.addAttribute("listaLivros", dao.listar());
        return "listarlivro";
    }

    @GetMapping("/alterarlivro")
    public String alterarLivro(HttpServletRequest req,  Model model) {
        int codigo = Integer.parseInt(req.getParameter("codigo"));
        LivroDao dao = new LivroDao();
        //Data Acess Object
        model.addAttribute("livro", dao.getLivroPorCodigo(codigo));
        return "alterarlivro";
    }

    @GetMapping("/alterar")
    public String alterar(@ModelAttribute("livro") Livro livro, Model model) {
        LivroDao dao = new LivroDao();
        model.addAttribute("mensagem", dao.salvar(livro));
        return "mensagem";
    }

    @GetMapping("/pesquisar")
    public String pesquisar(HttpServletRequest req, Model model) {
        String descricao = req.getParameter("descricao");
        LivroDao dao = new LivroDao();
        model.addAttribute("listaLivros", dao.getLivroPorTitulo(descricao));
        // model.addAttribute("listaLivros", dao.listar());
        return "listarlivro";
    }

    @GetMapping("/excluir")
    public String excluir(HttpServletRequest req, Model model) {
        int codigo = Integer.parseInt(req.getParameter("codigo"));
        LivroDao dao = new LivroDao();
        model.addAttribute("mensagem", dao.excluir(codigo));
        return "mensagem";
    }

}
