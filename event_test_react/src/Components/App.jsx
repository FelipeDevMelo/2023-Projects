import React from "react";
import { useState } from "react";

function App() {
  const [isMouseOver, setIsMouseOver] = useState(false);
  const [input, setInput] = useState("");
  const [headingTxt,SetHeadiongTxt] = useState("")

  function HandleChange(event) {
    setInput(event.target.value);
  }

  return (
    <div className="container">
      <h1>Hello {headingTxt}</h1>
      <input
        onChange={HandleChange}
        value={input}
        type="text"
        placeholder="What's your name?"
      />
      <button
        style={{ backgroundColor: isMouseOver ? "black" : "white" }}
        onMouseOut={() => setIsMouseOver(false)}
        onMouseOver={() => setIsMouseOver(true)}
        onClick={()=> SetHeadiongTxt(input)}
      >
        Submit
      </button>
    </div>
  );
}

export default App;
