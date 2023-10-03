import React from "react";
import { useState } from "react";

function App() {
  const [time, setTime] = useState("Time");

  return (
    <div className="container">
      <h1>{time}</h1>
      <button onClick={() => setTime(new Date().toLocaleTimeString())}>
        Get Time
      </button>
    </div>
  );
}

export default App;
