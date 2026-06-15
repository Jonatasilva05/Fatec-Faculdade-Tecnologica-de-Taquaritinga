import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Link, useNavigate } from 'react-router-dom';

function Dashboard() {
  const [users, setUsers] = useState([]);
  const navigate = useNavigate();

  const fetchUsers = async () => {
    try {
      const res = await axios.get('http://localhost:5000/users');
      setUsers(res.data);
    } catch (error) {
      console.error("Erro ao buscar usuários");
    }
  };

  const handleDelete = async (id) => {
    if (confirm('Tem certeza que deseja excluir?')) {
      await axios.delete(`http://localhost:5000/users/${id}`);
      fetchUsers();
    }
  };

  const handleLogout = () => {
    localStorage.removeItem('auth');
    navigate('/');
  };

  useEffect(() => { fetchUsers(); }, []);

  return (
    <div className="bg-light min-vh-100">
      {/* Barra de Navegação */}
      <nav className="navbar navbar-dark bg-dark mb-4">
        <div className="container">
          <span className="navbar-brand">Sistema Seguro</span>
          <button onClick={handleLogout} className="btn btn-outline-light btn-sm">Sair</button>
        </div>
        <div>
    <Link to="/admins" className="btn btn-outline-info btn-sm me-2">Gerenciar Logins</Link>
    <button onClick={handleLogout} className="btn btn-outline-light btn-sm">Sair</button>
</div>
      </nav>

      <div className="container">
        <div className="d-flex justify-content-between align-items-center mb-4">
          <h2>Usuários</h2>
          <Link to="/novo" className="btn btn-success">+ Novo Usuário</Link>
        </div>

        <div className="card shadow-sm">
          <div className="card-body p-0">
            <table className="table table-striped table-hover mb-0">
              <thead className="table-dark">
                <tr>
                  <th>ID</th>
                  <th>Nome</th>
                  <th>Email</th>
                  <th className="text-end">Ações</th>
                </tr>
              </thead>
              <tbody>
                {users.map(user => (
                  <tr key={user.id}>
                    <td>{user.id}</td>
                    <td>{user.name}</td>
                    <td>{user.email}</td>
                    <td className="text-end">
                      <Link to={`/editar/${user.id}`} className="btn btn-sm btn-warning me-2">
                        Editar
                      </Link>
                      <button onClick={() => handleDelete(user.id)} className="btn btn-sm btn-danger">
                        Excluir
                      </button>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  );
}
export default Dashboard;