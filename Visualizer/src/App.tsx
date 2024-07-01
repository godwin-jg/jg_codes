import { useState } from "react";
import reactLogo from "./assets/react.svg";
import viteLogo from "/vite.svg";
import "./App.css";
import Sorting from "./sorting/sort";

function App() {
  const [count, setCount] = useState(0);

  return (
    <div>
      <Sorting></Sorting>
    </div>
  );
}

export default App;
