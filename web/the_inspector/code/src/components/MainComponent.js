import React from 'react';
import "../styles.css"

const MainComponent = () => {
  return (
    <div className="hacking-page">
      <header className="header">
        <h1 className="title">InfoSec World</h1>
      </header>
      <main className="main-content">
        <p className="intro">Welcome to the fascinating world of hacking, where knowledge and creativity come together to create a better, safer digital world.</p>
        <p className="description">Discover the latest advancements in the field, learn from the experts, and share your ideas and insights with others who share your passion.</p>
      </main>
      <footer className="footer">
        <p>&copy; InfoSec World 2023</p>
      </footer>
    </div>
  );
};

export default MainComponent;
