package app.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class LivroController {
    
    @GetMapping("/cadastrar")
    public String cadastrar(){
        return "cadastrarlivro";
    }
}
