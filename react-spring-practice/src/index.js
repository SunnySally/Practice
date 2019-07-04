import React from "react";
import ReactDOM from "react-dom";
import "./styles.css";
import { useSpring, animated, interpolate, useMeasure, useSprings } from "react-spring";


function App() {
  // const props = useSpring({ opacity: 1, from: { opacity: 0 } });

  // const { o, xyz, color, a } = useSpring({
  //   from: { o: 0, xyz: [0, 0, 0], color: 'red', a: 0 },
  //   o: 1, xyz: [10, 20, 5], color: 'green', a: 2
  // })

  // return <animated.div style={{
  //   background: props.opacity.interpolate(o => `rgba(210, 57, 77, ${o})`),
  // }}>I will fade in</animated.div>;
  // return (
  //   <animated.div
  //     style={{
  //       // If you can, use plain animated values like always, ...
  //       // You would do that in all cases where values "just fit"
  //       color,
  //       // Unless you need to interpolate them
  //       background: o.interpolate(o => `rgba(210, 57, 77, ${o})`),
  //       // Which works with arrays as well
  //       transform: xyz.interpolate((x, y, z) => `translate3d(${x}px, ${y}px, ${z}px)`),
  //       // If you want to combine multiple values use the "interpolate" helper
  //       border: interpolate([o, color], (o, c) => `${o * 10}px solid ${c}`),
  //       // You can also form ranges, even chain multiple interpolations
  //       padding:
  //         o.interpolate({ range: [0, 0.5, 1], output: [0, 0, 10] })
  //           .interpolate(o => `${o}%`),
  //       // Interpolating strings (like up-front) through ranges is allowed ...
  //       borderColor: a.interpolate({ range: [0, 2], output: ['red', '#ffaabb'] }),
  //       // There's also a shortcut for plain, optionless ranges ...
  //       opacity: o.interpolate([0.1, 0.2, 0.6, 1], [1, 0.1, 0.5, 1]),
  //     }}>
  //     {o.interpolate(n => n.toFixed(2)) /* innerText interpolation ... */}
  //   </animated.div>
  // )

  // const props = useSpring({
  //   to: async (next, cancel) => {
  //     await next({ opacity: 1, color: '#ffaaee' })
  //     await next({ opacity: 0, color: 'blue' })
  //   },
  //   from: { opacity: 0, color: 'red' }
  // })
  // const props = useSpring({
  //   to: [{ opacity: 1, color: '#ffaaee' }, { opacity: 0, color: 'rgb(14,26,19)' }, { opacity: 1, color: 'rgb(14,26,19)' }],
  //   from: { opacity: 0, color: 'red' }
  // })
  // // ...
  // return <animated.div style={props}>I will fade in and out</animated.div>
  const num = 1
  const items = []
  const springs = useSprings(number, items.map(item => ({ opacity: item.opacity })))
  return (springs.map(props => <animated.div style={props} />))

}

const rootElement = document.getElementById("root");
ReactDOM.render(<App />, rootElement);