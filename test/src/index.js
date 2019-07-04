// import './index.css'
// import imgSource from './aaa.jpg'
// const component = document.createElement('div');
// component.innerHTML = 'Hello aaa'


// const img = new Image()
// img.src = imgSource
// document.body.appendChild(img);
// console.log(imgSource)

// const loadImage = (url) => {
//   return new Promise((resolve, reject) => {

//     const img = new Image()
//     img.onload = () => {
//       resolve(img)
//     }
//     img.onerror = () => {
//       reject(new Error('could not load image at' + url))
//     }
//     img.src = url
//   })
// }

// loadImage('./assets/img/aaa.jpg').then((img) => {
//   document.body.appendChild(img);
// }).catch((err) => {
//   console.log(err)
// })

// const getJson = (url) => {
//   return new Promise((resolve, reject) => {
//     const handler = function () {
//       if (this.readyState !== 4) {
//         return
//       }
//       if (this.status === 200) {
//         resolve(this.response)
//       } else {
//         console.log('err')
//         reject(new Error(this.statusText))
//       }

//     }
//     const client = new XMLHttpRequest()
//     client.open("GET", url)
//     client.onreadystatechange = handler;
//     client.responseType = 'json'
//     client.setRequestHeader('Accept', 'Application/json')
//     client.send()

//   })
// }

// const p1 = getJson('/data/province.json')
// const p2 = getJson('/data/world.json')
// const p3 = getJson('/data/cities.json')
// const pt = new Promise((resolve, reject) => {
//   setTimeout(() => {
//     reject(new Error('timeout'))
//   }, 2)
// })


// getJson('/data/province.json')
//   .then(result => {
//     console.log(result)
//   })
//   .catch(error => {
//     console.log(error)
//   })

// const p = Promise.all([p1, p2, p3]).then((d) => {
//   console.log(d)
// })

// const p = Promise.race([p1, pt]).then(console.log).catch(console.error)

// var fetch = require('node-fetch');

// function* gen() {
//   var url = 'https://api.github.com/users/github';
//   var result = yield fetch(url);
//   console.log(result);
// }
// var g = gen();
// var result = g.next();

// // result:{value: xxx, done: false}
// result.value.then(function (data) {
//   return data.json();
// }).then(function (data) {
//   g.next(data);
// });

