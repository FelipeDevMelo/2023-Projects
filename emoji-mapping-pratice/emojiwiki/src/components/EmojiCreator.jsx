import React from "react";
import Dictionary from "./Dictionary";


function EmojiCreator(emojiwiki) {
    return (
      <Dictionary
        key={emojiwiki.id}
        emoji={emojiwiki.emoji}
        name={emojiwiki.name}
        meaning={emojiwiki.meaning}
      />
    );
  }

  export default EmojiCreator;