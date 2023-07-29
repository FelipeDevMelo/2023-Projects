import axios from "axios";
import express from "express";
import bodyParser from "body-parser";
const app = express();

app.use(express.static("public"));
app.use(bodyParser.urlencoded({ extended: true }));

app.get("/", async (req, res) => {
  try {
    const pokemonNames = [];
    const pokemonGifs = [];
    const pokemonType = [];

    for (let index = 1; index < 15; index++) {
      const result = await axios.get(
        `https://pokeapi.co/api/v2/pokemon/${index}`
      );
      pokemonNames.push(result.data.name);
      pokemonGifs.push(result.data[`sprites`][`front_default`]);
      pokemonType.push(result.data[`types`][`0`][`type`][`name`]);
    }

    res.render("index.ejs", {
      pokemonNames: pokemonNames,
      pokemonGifs: pokemonGifs,
      pokemonType: pokemonType,
    });
  } catch (error) {
    console.log(error.response.data);
    res.status(500);
  }
});

app.post("/search", async (req, res) => {
   const id = req.body.id;
  
  try {
    const result = await axios.get(
      `https://pokeapi.co/api/v2/pokemon/${id}`
    );
       const pokemonName =result.data.name
      const  pokemonsprite=result.data[`sprites`][`front_default`]
      const  pokemonType=result.data[`types`][`0`][`type`][`name`]
      
    res.render("search.ejs", {
        id:id,
        pokemonName:pokemonName,
        pokemonType:pokemonType,
        pokemonsprite:pokemonsprite
        
    });
  } catch (error) {
    console.log(error.response.data);
    res.status(500);
  }
});
app.listen(3000, () => {
  console.log("server running on port 3000");
});
