package app.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import ch.qos.logback.core.model.Model;

@Controller
public class ContatoController {
    
    @GetMapping("/contato")
    public String contato(Model model) {
        return "contato";
    }
}
