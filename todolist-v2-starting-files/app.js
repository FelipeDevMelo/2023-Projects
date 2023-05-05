//jshint esversion:6
const mongoose = require("mongoose");
const express = require("express");
const bodyParser = require("body-parser");

const app = express();

app.set("view engine", "ejs");

app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static("public"));

main().catch((err) => console.log(err));

async function main() {
  await mongoose.connect("mongodb://127.0.0.1:27017/todolistDB");
}

const itemsSchema = new mongoose.Schema({
  name: String,
});

const Item = mongoose.model("item", itemsSchema);

const item1 = new Item({ name: "welcome to your todolist" });

const item2 = new Item({ name: "hit + to add a new item" });

const item3 = new Item({ name: "<--- hit this to delete an item>" });

const defaultItems = [item1, item2, item3];

app.get("/", function (req, res) {
  Item.find().then(function (foundItems) {
    if (foundItems.length === 0) {
      Item.insertMany(defaultItems);
      res.redirect("/");
    } else {
      res.render("list", { listTitle: "Today", newListItems: foundItems });
    }
  });
});
app.post("/", function (req, res) {
  const intemName = req.body.newItem;
  const item = new Item({
    name: intemName,
  });
  item.save();
  res.redirect("/")
});

app.get("/work", function (req, res) {
  res.render("list", { listTitle: "Work List", newListItems: workItems });
});

app.get("/about", function (req, res) {
  res.render("about");
});

app.listen(3000, function () {
  console.log("Server started on port 3000");
});
