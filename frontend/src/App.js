import React, { useState } from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import ChatBox from './ChatBox';
import LoginPage from './Login';
import RegisterPage from './Register';
import './App.css';

function App() {
  // Load user from localStorage on startup
  const [user, setUser] = useState(localStorage.getItem('user'));

  // When login succeeds, update localStorage and state
  const handleLogin = (username) => {
    localStorage.setItem('user', username);
    setUser(username);
  };

  // When user logs out
  const handleLogout = () => {
    localStorage.removeItem('user');
    setUser(null);
  };

  return (
    <Router>
      <div className="App">
        <h1 className="app-title">💬 Chemo Assistant Chatbot</h1>
        <Routes>
          <Route
            path="/"
            element={
              user ? <ChatBox onLogout={handleLogout} /> : <Navigate to="/login" />
            }
          />
          <Route path="/login" element={<LoginPage onLogin={handleLogin} />} />
          <Route path="/register" element={<RegisterPage />} />
          <Route path="*" element={<Navigate to="/" />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
