package app.controller;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PostMapping;

import app.dao.LivroDao;
import app.model.Livro;

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
        model.addAttribute("listaLivros", dao.listar())
        return "l"        
    }
}