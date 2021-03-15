import React, { useState, useEffect } from 'react';
import logo from './logo.svg';
import './App.css';

function App() {
  const [thing, setThing] = useState(0);

  useEffect(() => {
    fetch('/thing').then(res => res.json()).then(data => {
      setThing(data.thing);
    });
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
         <p>The current thing is {thing}.</p>
        </a>
      </header>
    </div>
  );
}

export default App;
