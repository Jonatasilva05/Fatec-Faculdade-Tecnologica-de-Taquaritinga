import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useNavigate, useParams, Link } from 'react-router-dom';

function FormUsuario() {
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const { id } = useParams();
  const navigate = useNavigate();

  useEffect(() => {
    if (id) {
      axios.get(`http://localhost:5000/users/${id}`)
        .then(res => {
          setName(res.data.name);
          setEmail(res.data.email);
        });
    }
  }, [id]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (id) {
      await axios.put(`http://localhost:5000/users/${id}`, { name, email });
    } else {
      await axios.post('http://localhost:5000/users', { name, email });
    }
    navigate('/dashboard');
  };

  return (
    <div className="bg-light min-vh-100">
      <nav className="navbar navbar-dark bg-dark mb-4">
        <div className="container">
          <span className="navbar-brand">Sistema Seguro</span>
        </div>
      </nav>

      <div className="container">
        <div className="row justify-content-center">
          <div className="col-md-6">
            <div className="card shadow">
              <div className="card-header bg-white">
                <h4 className="mb-0">{id ? 'Editar Usuário' : 'Novo Usuário'}</h4>
              </div>
              <div className="card-body">
                <form onSubmit={handleSubmit}>
                  <div className="mb-3">
                    <label className="form-label">Nome Completo</label>
                    <input 
                      className="form-control" 
                      value={name} 
                      onChange={e => setName(e.target.value)} 
                      required 
                    />
                  </div>
                  <div className="mb-3">
                    <label className="form-label">Email</label>
                    <input 
                      className="form-control" 
                      type="email"
                      value={email} 
                      onChange={e => setEmail(e.target.value)} 
                      required 
                    />
                  </div>
                  <div className="d-flex justify-content-between">
                    <Link to="/dashboard" className="btn btn-secondary">Cancelar</Link>
                    <button type="submit" className="btn btn-success">Salvar</button>
                  </div>
                </form>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
export default FormUsuario;