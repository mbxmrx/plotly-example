import Plot from "react-plotly.js";
import figure from "../figure.json";
import "./App.css";

function App() {
  return (
    <>
      <Plot {...figure} />
    </>
  );
}

export default App;
