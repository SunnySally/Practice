// class
var events = require("events");
var myEmitter = new events.EventEmitter();

myEmitter.on("someEvent", function(msg) {
  console.log(msg);
});

myEmitter.emit("someEvent", "the event is emitted");

// class
var util = require("util");

var Person = function(name) {
  this.name = name;
};

util.inherits(Person, events.EventEmitter);
var james = new Person("james");
var mary = new Person("mary");
var john = new Person("john");

var people = [james, mary, john];

people.forEach(function(person) {
  person.on("speak", function(msg) {
    console.log(`${person.name} said: ${msg}`);
  });
});

james.emit("speak", "hi, hhh");
mary.emit("speak", "sth");
john.emit("speak", "I'm john");

// class: fs
var stuff = require("./stuff");
console.log(stuff.counter("ddddd"));
console.log(stuff.add(5, 6));
console.log(stuff.pi);

// class fs
var fs = require("fs");
// var readMe = fs.readFileSync("readMe.txt", "utf8");
// console.log(readMe);
// fs.writeFileSync("writeMe.txt", readMe);

// fs.readFile("readMe.txt", "utf8", function(err, data) {
//   console.log(data);
//   fs.writeFile("writeMe.txt", data, err => {
//     if (err) throw err;
//     console.log("the file has been saved");
//   });
// });

// class: directories

// del file
// fs.unlink("writeMe.txt");

// sync
// fs.mkdirSync("stuff");
// fs.rmdirSync("stuff");

// async
// fs.mkdir("stuff", () => {
//   fs.readFile("readme.txt", "utf8", (err, data) => {
//     fs.writeFile("./stuff/writeMe.txt", data, err => {
//       if (err) throw err;
//       console.log("file has been saved in dir stuff");
//     });
//   });
// });

// fs.unlink("./stuff/writeMe.txt", () => {
//   fs.rmdir("stuff");
// });
