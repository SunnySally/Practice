import lottie from 'lottie-web'

const greeter = require("./greeter.js");
document.querySelector("#root").appendChild(greeter());

lottie.loadAnimation({
  container: element, // the dom element that will contain the animation
  renderer: 'svg',
  loop: true,
  autoplay: true,
  path: 'test.json' // the path to the animation json
});
