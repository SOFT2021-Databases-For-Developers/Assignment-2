const one = () => {
    let array = [1,9,16,100]
    let res = array.map(item => Math.sqrt(item))
    console.log(res)
}

const two = () => {
    let array =  ["Intro", "Requirements", "Analysis", "Implementation", "Conclusion", "Discussion",
        "References"]
    let res = array.map(item => "<h1>" + item + "</h1>")
    console.log(res)
}

const three = () => {
    let array = ["i'm", "yelling", "today"]
    let res = array.map(item => item.toUpperCase())
    console.log(res)
}

const four = () => {
    let array = ["I", "have", "looooooong", "words"]
    let res = array.map(item => item.length)
    console.log(res)
}

const five = () => {

}

function reduceAdder(total, num) {
    return total + num;
}

const six = () => {
    let array = [1,2,3,4,5]
    let res = array.reduce(reduceAdder)
    console.log(res)
}

function reduceX(sum, xObject) {
    return sum + xObject.x
}

const seven = () => {
    let array = [{x: 1}, {x: 2}, {x: 3}]
    let res = array.reduce(reduceX)
    console.log(res)
}

function reduceArrayFlatten(flatten, array) {
    array.map(item => flatten.push(item))
    return flatten
}

const eight = () => {
    let array = [[1,2], [3,4], [5,6]]
    let res = array.reduce(reduceArrayFlatten)
    console.log(res)
}

function reducePositiveNumbers(sumArray, number) {
    sumArray.push(number)
    return sumArray
}

const nine = () => {
    let array = [-3, -1, 2, 4, 5]
    let res = array.reduce(reducePositiveNumbers)
    console.log(res)
}
var count = 0
console.log("-------[" + (++count) +"]--------")
one()
console.log("-------[" + (++count) +"]--------")
two()
console.log("-------[" + (++count) +"]--------")
three()
console.log("-------[" + (++count) +"]--------")
four()
console.log("-------[" + (++count) +"]--------")
five()
console.log("-------[" + (++count) +"]--------")
six()
console.log("-------[" + (++count) +"]--------")
seven()
console.log("-------[" + (++count) +"]--------")
eight()
console.log("-------[" + (++count) +"]--------")
//nine()