const express = require('express');
const mysql = require('mysql2');
const cors = require('cors');

const app = express();
app.use(cors());
app.use(express.json());

const db = mysql.createPool({
  host: 'db', user: 'root', password: 'passwordroot', database: 'meubanco'
});

// --- ROTA DE LOGIN (Agora busca no Banco) ---
app.post('/login', (req, res) => {
  const { email, password } = req.body;
  // ATENÇÃO: Em produção real, use bcrypt para hash de senhas!
  const sql = "SELECT * FROM admins WHERE email = ? AND password = ?";
  
  db.query(sql, [email, password], (err, result) => {
    if (err) return res.status(500).json(err);
    
    if (result.length > 0) {
      res.json({ auth: true, token: 'token-seguro-bd', user: result[0] });
    } else {
      res.status(401).json({ auth: false, message: 'Credenciais inválidas' });
    }
  });
});

// --- CRUD DE USUÁRIOS COMUNS (Mantido igual) ---
app.post('/users', (req, res) => { /* ...seu código anterior... */ 
    const { name, email } = req.body;
    db.query("INSERT INTO users (name, email) VALUES (?, ?)", [name, email], (err) => {
        if(err) return res.status(500).json(err);
        res.json({message: 'Criado'});
    });
});
app.get('/users', (req, res) => {
    db.query('SELECT * FROM users', (err, result) => res.json(result));
});
app.get('/users/:id', (req, res) => {
    db.query('SELECT * FROM users WHERE id = ?', [req.params.id], (err, result) => res.json(result[0]));
});
app.put('/users/:id', (req, res) => {
    const { name, email } = req.body;
    db.query("UPDATE users SET name = ?, email = ? WHERE id = ?", [name, email, req.params.id], (err) => res.json({message:'Ok'}));
});
app.delete('/users/:id', (req, res) => {
    db.query('DELETE FROM users WHERE id = ?', [req.params.id], (err) => res.json({message:'Del'}));
});

// --- NOVO: CRUD DE ADMINS (Para criar novos logins) ---
app.get('/admins', (req, res) => {
    db.query('SELECT * FROM admins', (err, result) => res.json(result));
});
app.post('/admins', (req, res) => {
    const { email, password } = req.body;
    db.query("INSERT INTO admins (email, password) VALUES (?, ?)", [email, password], (err) => {
        if(err) return res.status(500).json(err);
        res.json({message: 'Admin criado'});
    });
});
// Rota para mudar senha/email de admin
app.put('/admins/:id', (req, res) => {
    const { email, password } = req.body;
    db.query("UPDATE admins SET email = ?, password = ? WHERE id = ?", [email, password, req.params.id], (err) => res.json({message:'Admin Atualizado'}));
});

app.listen(5000, () => console.log('Servidor Rodando'));