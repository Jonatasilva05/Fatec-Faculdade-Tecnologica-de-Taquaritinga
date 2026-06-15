// ESSE ARQUIVO É O NOSSO SERVIDOR, RESPONSAVEL POR SUBIR TUDO "ONLINE"

import express from 'express';
import userRoutes from './routes.js';

const app = express();
app.use(express.json()); // PARA O EXPRESS ENTENDER QUE É UMA BIBLIOTECA DE JSON


app.use('/usuarios', userRoutes)


app.listen(3000, () => {
    console.log('Servidor Online na porta 3000');
    },
);









// QUANDO FORMOS EXECUTAR O SERVIDOR É BOM USAR O --WATCH PARA ELE FICAR REINICIANDO AUTOMATICAMENTE
// node --watch src/server.js