import './Styles.css';
import React from 'react';

function App() {
  const graphInfoForm = () => (
    <div className="inputForm">
      <input
        type="text"
        placeholder="Número de Vértices"
      />
      <input
        type="text"
        placeholder="Número de Arestas"
      />
    </div>
  )

  return (
    <div className="header">
      <h1>Graphs is fun!</h1>
      <div className="subtitle">Este projeto serve para mostrar um pouco das muitas funcionalidades de grafos
        e também para mostrar o quão divertido "brincar" com grafos pode ser.
      </div>
      <div>{graphInfoForm()}</div>
    </div>
  );
}

export default App;
