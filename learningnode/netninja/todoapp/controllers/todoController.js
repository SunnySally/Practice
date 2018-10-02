var bodyParser = require("body-parser");
var mongoose = require('mongoose')

// connect to the database
mongoose.connect('mongodb://test:test123@ds145072.mlab.com:45072/todoapp')

// create a schema
var todoSchema = new mongoose.Schema({
  item: String
})

// model
var Todo = mongoose.model('strange', todoSchema)

var urlencodedParser = bodyParser.urlencoded({ extended: false });

module.exports = app => {
  app.get("/todo", (req, res) => {
    // get data from mongodb
    Todo.find({}, (err, data) => {

      if (err) throw err
      res.render("todo", { todos: data });
    })

  });

  app.post("/todo", urlencodedParser, (req, res) => {
    // get data from the view and add it to mongodb
    var newTodo = Todo(req.body).save((err, data) => {
      if (err) throw err
      res.json(data);
    })
  });

  app.delete("/todo/:item", (req, res) => {
    // delete the requested item from mongodb
    Todo.find({ item: req.params.item.trim() }).remove((err, data) => {
      if (err) throw err
      res.json(data);
    })

  });
};
