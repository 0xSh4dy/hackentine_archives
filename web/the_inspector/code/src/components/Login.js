import React, { useState } from 'react';
import Navbar from './Navbar';

const LoginPage = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const desiredUsername = "tit4n";
  const desiredPass = "tit4n5'Secr3t"

  function getFlag(){
    return atob("VlVMTlRJTkV7SDRjazNyX0VsMXRlXzIwMjN9");
  }
  const handleSubmit = (event) => {
    event.preventDefault();
    if(atob(username)==desiredUsername && atob(password)==desiredPass){
        window.alert(getFlag());
    }
    else{
        alert("Incorrect credentials");
    }
  };

  return (
    <div>
      <Navbar />

    <div style={{ backgroundImage: "url('https://thumbs.dreamstime.com/b/hacker-computer-cyber-attack-concept-background-83886543.jpg')", backgroundSize: 'cover', height: '100vh', display: 'flex', justifyContent: 'center', alignItems: 'center' }}>
      <div style={{ backgroundColor: '#42297A',opacity:0.9, padding: '2rem', borderRadius: '10px', width: '30%', display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
        <form onSubmit={handleSubmit} style={{ display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
          <h2 style={{ color: 'white', marginBottom: '1rem' }}>Secret Vault</h2>
          <input
            type="text"
            placeholder="Username"
            value={username}
            onChange={(event) => setUsername(event.target.value)}
            style={{ padding: '0.5rem', marginBottom: '1rem', borderRadius: '5px', border: 'none', backgroundColor: 'white', color: 'blue' }}/>
          <input
            type="password"
            placeholder="Password"
            value={password}
            onChange={(event) => setPassword(event.target.value)}
            style={{ padding: '0.5rem', marginBottom: '1rem', borderRadius: '5px', border: 'none', backgroundColor: 'white', color: 'blue' }}
          />
          <button type="submit" style={{ backgroundColor: 'rgba(255, 255, 255, 0.2)', color: 'white', padding: '0.5rem', borderRadius: '5px', border: 'none', marginTop: '1rem' }}>
            Login
          </button>
        </form>
      </div>
    </div>
    </div>
  );
};

export default LoginPage;
