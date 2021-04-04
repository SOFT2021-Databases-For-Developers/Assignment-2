const one = () => {
    let array = [1,9,16,100]
    array.map(item => item.sqrt())
}

const two = () => {
    let array =  ["Intro", "Requirements", "Analysis", "Implementation", "Conclusion", "Discussion",
        "References"]
    array.map(item => "<h1>" + item + "</h1>")
}

const three = () => {
    let array = ["i'm", "yelling", "today"]
    array.map(item => item.toUpperCase())
}

const four = () => {
    let array = ["I", "have", "looooooong", "words"]
    array.map(item => item.length)
}

const five = () => {

}

function reduceAdder(total, num) {
    return total + num;
}

const six = () => {
    let array = [1,2,3,4,5]
    array.reduce(reduceAdder)
}

function reduceX(sum, xObject) {
    return sum + xObject.x
}

const seven = () => {
    let array = [{x: 1}, {x: 2}, {x: 3}]
    array.reduce(reduceX)
}

function reduceArrayFlatten(flatten, array) {
    array.map(item => flatten.push(item))
    return flatten
}

const eight = () => {
    let array = [[1,2], [3,4], [5,6]]
    array.reduce(reduceArrayFlatten)
}

function reducePositiveNumbers(sumArray, array) {
    array.map(item => {
        if(item => 0)
        {
            sumArray.push(item)
        }
    })
    return sumArray
}

const nine = () => {
    let array = [-3, -1, 2, 4, 5]
    array.reduce(reducePositiveNumbers)
}