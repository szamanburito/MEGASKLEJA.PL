import React from 'react';
import { Routes, Route } from "react-router-dom";
import './App.css';
import Home from '../Home';
import Contact from '../Contact';
import { Navbar, Nav } from "react-bootstrap";

function App() {
  return (
    <div className="App">
      <header className="App-header">
      <Navbar bg="primary" variant="dark">
          <Nav.Link href="/home">Home</Nav.Link>
          <Nav.Link href="/contact">Contact</Nav.Link>
      </Navbar>
      </header>
      <body className="App-container">
                <Routes>
                    <Route path="/home" element={<Home />} />
                    <Route path="/contact" element={<Contact />} />
                </Routes>
      </body>
      
    </div>
  );
}

export default App;
