import './Styles.css';
import React from 'react';
import { Stage, Layer, Arrow, Circle, Text } from "react-konva";

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

  const renderGraph = () => (
    <div className="graph-container">
      <Stage width={900} height={900} className="graphView">
        {/* <Layer>
          {renderEdges(graph_matrix)}
          {renderVertex(graph_matrix)}
        </Layer> */}
      </Stage>
    </div>
  );

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
