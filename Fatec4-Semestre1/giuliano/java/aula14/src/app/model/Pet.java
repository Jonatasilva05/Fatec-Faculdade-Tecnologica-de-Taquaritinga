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
    private String tutor;
    private String raca;
    private String celular;
}

/* 
CREATE TABLE pet (
 codigo INTEGER NOT NULL AUTO_INCREMENT,
 nome VARCHAR (100),
 tutor VARCHAR (100),
 raca VARCHAR (100),
 celular VARCHAR (25),
 CONSTRAINT pk_pet PRIMARY KEY (codigo)
 )ENGINE=INNODB;

);


*/
