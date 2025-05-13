package app.controller;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

import app.model.Contato;

@Controller
public class ContatoController {
    
    @GetMapping("/contato")
    public String contato(Model model) {
        Contato c = new Contato();
        model.addAttribute("listaContatos", c.getContatos());
        return "contato";
    }
}
