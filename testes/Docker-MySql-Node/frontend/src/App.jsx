import React from 'react';
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import Login from './Login';
import Dashboard from './Dashboard';
import FormUsuario from './FormUsuario';
import AdminManager from './AdminManager'; // <--- ESTA LINHA ESTAVA FALTANDO!

function App() {
  const isAuthenticated = () => localStorage.getItem('auth') === 'true';

  const PrivateRoute = ({ children }) => {
    return isAuthenticated() ? children : <Navigate to="/" />;
  };

  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/dashboard" element={<PrivateRoute><Dashboard /></PrivateRoute>} />
        <Route path="/novo" element={<PrivateRoute><FormUsuario /></PrivateRoute>} />
        <Route path="/editar/:id" element={<PrivateRoute><FormUsuario /></PrivateRoute>} />
        
        {/* Rota para Gerenciar Admins */}
        <Route path="/admins" element={<PrivateRoute><AdminManager /></PrivateRoute>} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;