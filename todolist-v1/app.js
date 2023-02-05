//jshint esversion:6

const express = require("express");
const bodyParser = require("body-parser");

const app = express();
app.use(bodyParser.urlencoded({ extended: false }));
app.use(express.static("public"));
app.set("view engine", "ejs");
let itemsArray = [];




app.get("/", function (req, res) {
  const date = new Date();

  let options = {
    weekday: "long",
    day: "numeric",
    month: "long",
  };

  res.render("list", {newListItem:itemsArray, dateEJS: date.toLocaleDateString("en-US", options) });
});


app.post("/", function (req, res) {
 item = req.body.newItem;
 itemsArray.push(item);
  res.redirect("/");
 
 });


app.listen(3000, function () {
  console.log("server is running on port 3000");
});
