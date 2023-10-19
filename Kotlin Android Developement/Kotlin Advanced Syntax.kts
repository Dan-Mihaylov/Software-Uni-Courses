// Defining a basic function that takes parameters

fun myFunction(
    firstParam: Int,
    secondParam: String,
    thirdParam: Boolean
): String {
    return "First Parameter: $firstParam, Second Parameter: $secondParam, Third Parameter: $thirdParam"
}

myFunction(2, "My string", true)

fun newFunction(
    a: Int,
    b: Int,
    add: Boolean
): Int {
    if (add){
        return a + b
    }
    return a - b
}

val result =  newFunction(a=10, b=5, add=true)
println(result)

// Lambda functions, we can pass the as parameters to other functions

val lambdaFunction = {a: Int, b: Int -> a + b}
lambdaFunction(2, 5)

val subtractFunction = {a: Int, b: Int -> a - b}
subtractFunction(10, 5)

val anonymousFun = fun(a: Int, b: Int): Int {
    return a + b
}

fun doMathFunction (
    a: Int,
    b: Int,
    mathOperation: (Int, Int) -> Int    // This is how you pass a func as a parameter (type, type) -> res
) : Int {
    return (mathOperation(a, b))
}

doMathFunction(10, 2, subtractFunction)

// or different syntax to call the function with a parameter other func

doMathFunction(10, 5){a: Int, b: Int -> a + b}

val numbers = arrayOf(1, 2, 3, 4, 5, 6)
val onlyEvens =  numbers.filter { it % 2 == 0 }  // Can access the items in the lambda filter function by keyword it.
val sortedDescendingOrder =  numbers.sortedBy { -it }
val transformingValue = numbers.map { it * it }

onlyEvens
sortedDescendingOrder
transformingValue

// Single line functions

val singleLineFunction = fun (a: Int, b: Int) = a + b
singleLineFunction(5, 5)

val singleLineSubtraction = fun (a: Int, b: Int) = a - b
singleLineSubtraction(10, 2)

// Tail recursive functions, functions that call themselves recursively, they have been optimised
// not to run out of memory as a regular recursive function will.

tailrec fun someRecursiveFunction(x: Int): Int {
    val newX = x + 1
    return if (newX == 10)
        newX
    else
        someRecursiveFunction(newX)
}

someRecursiveFunction(1)

// Infix functions, extent the functionality of some class, then you can call them
// using simple language like  this plus that

infix fun Int.plus(that: Int): Int {
    return this + that
}

val a = 10
val b = 5

a plus b

infix fun Int.minus(that: Int): Int {
    return this - that
}

a minus b


// Extension functions

fun HashMap<Int, String>.description(): String {
    var description = ""

    for (entry in this.entries) {
        description += "${entry.key} => ${entry.value}\n"
    }
    return description
}

val myHashMap = HashMap<Int, String>()
myHashMap[1] = "one"
myHashMap[2] = "two"
myHashMap.description()

