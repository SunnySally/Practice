// var fs = require('fs');

// var read = thunkify(fs.readFile);
// read('package.json')(function (err, str) {
//   console.log(str)
// });

// function thunkify(fn) {
//   return function () {
//     var args = new Array(arguments.length);

//     var ctx = this;

//     for (var i = 0; i < args.length; ++i) {
//       args[i] = arguments[i];
//     }

//     return function (done) {
//       var called;

//       args.push(function () {
//         if (called) return;
//         called = true;
//         done.apply(null, arguments);
//       });

//       try {
//         fn.apply(ctx, args);
//       } catch (err) {
//         done(err);
//       }
//     }
//   }
// };

var fs = require('fs');
var thunkify = require('thunkify');
var readFileThunk = thunkify(fs.readFile);
var co = require('co')

var gen = function* () {
  var r1 = yield readFileThunk('./data/a.json');
  console.log(r1.toString());
  var r2 = yield readFileThunk('./data/b.json');
  console.log(r2.toString());
};


/**
 * 下面函数不适合异步，会返回  Cannot read property 'toString' of undefined
 */

// var g = gen();
// var res = g.next();

// while (!res.done) {
//   console.log(res.value);
//   res = g.next();
// }

// function run(fn) {
//   var gen = fn();

//   function next(err, data) {

//     var result = gen.next(data);
//     console.log(111, data, result)
//     // result.value就是yield返回的thunk包装函数，需要接受一个回调函数作为参数
//     if (result.done) return;
//     result.value(next);
//   }

//   next();
// }

// run(gen)


/**
 * `thunkify`模块作用：
 * 把需要传2个参数，第2个参数是回调函数的函数，包装成调用2次的函数，第2次用来调用回调函数
 */


/**
 * `co`依次执行异步操作的步骤：
 * 0. yield后面需要返回的是一个异步操作函数，被处理成一个promise函数
 * 1. 调用`next()`，得到`result: { value: { promise函数 }; done: false }`,如果done为true, 返回`resolve(value)`
 * 2. 调用`value.then()`, 在内部再调用一次`next()`，也就是在第一个promise结束之后再调用下一个异步操作，循环1，2直到resolve
 */
// co(gen)



// const stream = fs.createReadStream('./data/world.json');
// let chinaCount = 0;

// co(function* () {
//   while (true) {
//     const res = yield Promise.race([
//       new Promise(resolve => stream.once('data', resolve)),
//       new Promise(resolve => stream.once('end', resolve)),
//       new Promise((resolve, reject) => stream.once('error', reject))
//     ]);
//     if (!res) {
//       break;
//     }
//     stream.removeAllListeners('data');
//     stream.removeAllListeners('end');
//     stream.removeAllListeners('error');
//     console.log(res)
//     chinaCount += (res.toString().match(/china/ig) || []).length;
//   }
//   console.log('count:', chinaCount);
// });


const asyncReadFile = async function () {
  const f1 = await fs.readFile('./data/a.json');
  const f2 = await fs.readFile('./data/b.json');
  // console.log(f1.toString());
  // console.log(f2.toString());
  // 这里返回的是promise中resolve的参数
  console.log(f1)
  return f1
};

const f = asyncReadFile().then(value => {
  console.log('resolve', value)
})
