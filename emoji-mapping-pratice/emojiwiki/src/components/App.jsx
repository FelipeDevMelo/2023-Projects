import React from "react";
import Dictionary from "./Dictionary";
import emojipedia from "../emojipedia";

function App() {
  return (
    <div>
      <h1>
        <span>emojipedia</span>
      </h1>
      {emojipedia.map((emojiwiki) => (
        <Dictionary
          key={emojiwiki.id}
          emoji={emojiwiki.emoji}
          name={emojiwiki.name}
          meaning={emojiwiki.meaning}
        />
      ))}
    </div>
  );
}

export default App;
