import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Link } from 'react-router-dom';

function AdminManager() {
  const [admins, setAdmins] = useState([]);
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const fetchAdmins = async () => {
    const res = await axios.get('http://localhost:5000/admins');
    setAdmins(res.data);
  };

  useEffect(() => { fetchAdmins(); }, []);

  const handleCreate = async (e) => {
    e.preventDefault();
    await axios.post('http://localhost:5000/admins', { email, password });
    setEmail(''); setPassword('');
    fetchAdmins();
    alert('Novo login criado!');
  };

  return (
    <div className="container mt-5">
      <h2>Gerenciar Acessos (Logins)</h2>
      <Link to="/dashboard" className="btn btn-secondary mb-4">Voltar ao Dashboard</Link>

      <div className="row">
        {/* Formulário de Novo Admin */}
        <div className="col-md-5">
          <div className="card p-3 shadow-sm">
            <h5>Novo Administrador</h5>
            <form onSubmit={handleCreate}>
              <input className="form-control mb-2" placeholder="Email de Login" value={email} onChange={e=>setEmail(e.target.value)} />
              <input className="form-control mb-2" placeholder="Senha" value={password} onChange={e=>setPassword(e.target.value)} />
              <button className="btn btn-primary w-100">Adicionar Acesso</button>
            </form>
          </div>
        </div>

        {/* Lista de Admins */}
        <div className="col-md-7">
          <table className="table table-bordered bg-white">
            <thead><tr><th>ID</th><th>Login (Email)</th><th>Senha</th></tr></thead>
            <tbody>
              {admins.map(admin => (
                <tr key={admin.id}>
                  <td>{admin.id}</td>
                  <td>{admin.email}</td>
                  <td>****</td> {/* Por segurança, não mostre a senha na tela */}
                </tr>
              ))}
            </tbody>
          </table>
          <small className="text-muted">Use o PhpMyAdmin para editar senhas existentes.</small>
        </div>
      </div>
    </div>
  );
}
export default AdminManager;