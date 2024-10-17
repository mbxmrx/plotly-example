import Plot, { PlotParams } from "react-plotly.js";
import figureJson from "../figure.json";
import "./App.css";

const figure = figureJson as unknown as PlotParams;

export function App() {
  return <Plot {...figure} />;
}
