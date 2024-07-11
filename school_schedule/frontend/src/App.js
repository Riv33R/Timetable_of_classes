import React from 'react';
import Schedule from './components/Schedule';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>School Schedule</h1>
      </header>
      <main>
        <Schedule />
      </main>
    </div>
  );
}

export default App;
