import React from "react";
import EmojiCreator from "./EmojiCreator";
import emojipedia from "../emojipedia";


function App() {
  return (
    <div>
      <h1>
        <span>emojipedia</span>
      </h1>
      {emojipedia.map(EmojiCreator)}
    </div>
  );
}

export default App;
