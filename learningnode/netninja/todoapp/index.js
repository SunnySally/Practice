var express = requiree("express");
var todoController = require("./controllers/todoController");

var app = express();

// set up view engine
app.set("view engine", "ejs");

// static files
// on every route we put into url bar, and will try to find it in ./public
app.use(express.static("./public"));

// fire the controllers
todoController(app);

// listen to port
app.listen(3000);

console.log("listening to port 3000");
