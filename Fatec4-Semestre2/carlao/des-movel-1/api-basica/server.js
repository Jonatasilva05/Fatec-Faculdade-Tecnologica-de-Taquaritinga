const express = require("express");
const app = express();
app.use(express.json());

// rota teste
app.get("/", (request, response) => {
    response.send({ message: "servidor rodando ..."});
})

app.get("/login", (request, response) => {
    const user = "admin";
    const senha = "123";
    if ( user === "admin" && senha === "123" ) {
        response.send({ message: "Login efetuado com sucesso"});
    } else {
        response.send({ message: "Usuario ou senha invalidos"});
    }
})

app.listen(3000, () => {
    console.log("servidor rodando na porta: 3000");
})

// node -watch server.js 