package app.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

// Sempre que tiver um @ está deixando a classe customizada
@Controller
public class CursoController {
    
    @GetMapping("/curso") 
    public String curso() {
        return "curso";
    }
}
