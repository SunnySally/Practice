import * as pointLayouts from './layouts.js'
import * as d3 from 'd3'
import styles from './index.less'

// canvas settings
const width = 600
const height = 600

// point settings
const numPoints = 7000
const pointWidth = 4
const pointMargin = 3

// animation settings
const duration = 1500
const ease = d3.easeCubic
let timer
let currentLayout = 0

// create set of points
const points = pointLayouts.createPoints(numPoints, pointWidth, width, height)
const toGrid = points => pointLayouts.gridLayout(points,
  pointWidth + pointMargin, width)
const toSine = points => pointLayouts.sineLayout(points,
  pointWidth + pointMargin, width, height)
const toSpiral = points => pointLayouts.spiralLayout(points,
  pointWidth + pointMargin, width, height)
const toPhyllotaxis = points => pointLayouts.phyllotaxisLayout(points,
  pointWidth + pointMargin, width / 2, height / 2)

// store the layouts in an array
const layouts = [toSine, toPhyllotaxis, toSpiral, toPhyllotaxis, toGrid]

// draw the points based on their current layout
function draw() {
  const ctx = canvas.node().getContext('2d')
  ctx.save()

  // erase what is draw on the canvas currently
  ctx.clearRect(0, 0, width, height)
  points.map((point) => {
    ctx.fillStyle = point.color
    ctx.fillRect(point.x, point.y, pointWidth, pointWidth)
  })

  ctx.restore()
}

// animate the points to a given layout
const animate = (layout) => {
  // store the source position
  points.forEach(point => {
    point.sx = point.x
    point.sy = point.y
  })

  // get the destination layout
  layout(points)

  // store the destination layout
  points.forEach(point => {
    point.tx = point.x
    point.ty = point.y
  })

  // timer is called regularly
  timer = d3.timer(elapsed => {
    // compute the progress of the this animation process
    let t = Math.min(1, ease(elapsed / duration))
    // update the position of points
    points.forEach(point => {
      point.x = point.sx * (1 - t) + point.tx * t
      point.y = point.sy * (1 - t) + point.ty * t
    })
    // update the canvas
    draw()
    // if this animation process is over
    // go to next animatin process
    if (t === 1) {
      // stop the timer for this layout and start a new one
      timer.stop()
      // use the next layout
      currentLayout = (currentLayout + 1) % layouts.length
      // start the animation of next layout
      animate(layouts[currentLayout])
    }
  })
}

// create canvas
const canvasDiv = d3.select('body')
  .append('div')
  .attr('class', 'canvas')
  .on('click', () => {
    // stop animate
    timer.stop()
    maskDiv.style('display', 'flex')
  })

const canvas = canvasDiv.append('canvas')
  .attr('width', width)
  .attr('height', height)

// draw the initial view
toGrid(points);
draw();
const maskDiv = d3.select('body')
  .append('div')
  .attr('class', 'mask')
  .on('click', () => {
    // start animate
    animate(layouts[currentLayout])
    maskDiv.style('display', 'none')
  })
maskDiv.append('div')
  .text('Start')