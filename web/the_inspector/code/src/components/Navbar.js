import React from 'react';


const Navbar = () => {
  return (
    <nav className="navbar" style={{ backgroundColor: '#42297A', color: 'white', padding: '1rem', display: 'flex', justifyContent: 'space-between' }}>
      <div className="brand" style={{ fontSize: '1.5rem', fontWeight: 'bold' }}>
        InfoSec World
      </div>
      <ul className="navbar-nav" style={{ display: 'flex', listStyle: 'none', margin: 0, padding: 0 }}>
        <li className="nav-item" style={{ marginRight: '1rem' }}>
          <a href='/' className="nav-link" style={{ color: 'white', textDecoration: 'none' }}>Home</a>
        </li>
        <li className="nav-item" style={{ marginRight: '1rem' }}>
          <a href="/login" className="nav-link" style={{ color: 'white', textDecoration: 'none' }}>Login</a>
        </li>
      </ul>
    </nav>
  );
};

export default Navbar;
