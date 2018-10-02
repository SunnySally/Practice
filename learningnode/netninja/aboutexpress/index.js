var express = require("express");
var bodyParser = require("body-parser");
var app = express();

var urlencodedParser = bodyParser.urlencoded({ extended: false });

app.set("view engine", "ejs");

// middleware between the req and the res
// the first params match the route, the second params link up to the directory
app.use("/assets", express.static("stuff"));

app.post("/contact", urlencodedParser, (req, res) => {
  console.log(req.body);
  res.render("contact-success", { data: req.body });
});

app.get("/", (req, res) => {
  res.render("index");
});

app.get("/contact", (req, res) => {
  res.render("contact", { qs: req.query });
});

app.get("/profile/:id", (req, res) => {
  var data = { age: 29, job: "ninja", hobbies: ["eating", "fishing"] };
  res.render("profile", { name: req.params.id, data: data });
});

//req obj contains query string but it does not handle the passing of the post data

app.listen(3000);
