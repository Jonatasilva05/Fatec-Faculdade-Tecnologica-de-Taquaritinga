package app.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class CursoController {
    
    @GetMapping("/curso")
    public String curso() {
        return "curso";
    }
}
