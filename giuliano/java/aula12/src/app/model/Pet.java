package app.model;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
public class Pet {
    private int codigo;    
    private String nome;
    private String telefone;
    private String nomepet;
}

/*
    CREATE TABLE pet (
        codigo INTEGER NOT NULL AUTO_INCREMENT,
        nome VARCHAR(100),
        valor NUMERIC(10, 2),
        CONSTRAINT pk_produto PRIMARY KEY (codigo)
    )ENGINE=INNODB;

*/