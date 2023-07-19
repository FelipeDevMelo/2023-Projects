const express = require("express");
const bodyParser = require("body-parser");
const ejs = require("ejs");
const mongoose = require("mongoose");
const app = express();
const port = 3000;

app.set("view engine", "ejs");

app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static("public"));
main().catch((err) => console.log(err));
async function main() {
  await mongoose.connect("mongodb://127.0.0.1:27017/wikiDB");
}

const articleSchema = new mongoose.Schema({
  title: String,
  content: String,
});

const Article = mongoose.model("Article", articleSchema);


////////////////////////////////////////////////

app.route("/articles/:articleTitle")

  .get((req, res) => {});


app
.route("/articles")

  .get((req, res) => {
    Article.find()
      .then(function (foundArticles) {
        res.send(foundArticles);
      })
      .catch(function (err) {
        console.log(err);
      });
  })

  .post((req, res) => {
    const newPost = new Article({
      title: req.body.title,
      content: req.body.content,
    });
    newPost.save();
  })

  .delete((req, res) => {
    Article.deleteMany()
      .then(function () {
        console.log("sucessfully deleted everything");
      })
      .catch(function (err) {
        console.log(err);
      });
  });



app.listen(port, () => {
  console.log(` app listening on port ${port}`);
});
