import java.util.Random



// When Statement

// Supports infinite number of cases with one default  value at the end.

val someVariable = 5

when (someVariable) {
    1 -> println("Its one")
    2 -> println("its two")
    else -> println("its not one its not two")
}


// Nested Lists

val array = ArrayList<ArrayList<Int>>()

for (i in 1 .. 3) {
    val nestedArray = ArrayList<Int>()
    for (j in 1 .. 3) {
        nestedArray.add(i * j)
    }
    array.add(nestedArray)
}
array
array[2][2]



outer@ for (i in 1..5) {
    inner@ for (j in 1..5) {
        if (j == 3) {
            break@outer
        }
        val res = i * j
        println(res)
    }
}


// Ints stream

val intsStream = Random().ints(10)
val intArray = ArrayList<Int>()

for (num in intsStream) {
    if (num > 0) {
        intArray.add(num)
        println("Added number because number $num is Positive")
    }
    else {
        println("Not Adding Number because Number $num is Negative")
    }
}

val someArray = ArrayList<Int>()
val random  = Random()
do {
    val nextValue = random.nextInt()
//    if (nextValue > 0) {
//        someArray.add(nextValue)
//    }
    someArray.add(nextValue)
} while (someArray.size < 10)

someArray

for (number in someArray) {
    if (number < 0) {
        println("($number) Is a negative")
    }
    else {
        println("The Number is positive $number")
    }
}





// Some more conditional statements
val a = Random().nextInt()
val isEven: Boolean = if (a == 0) {
    println("a is zero")
    true
}
else if (a % 2 == 0) {
    println("a is even")
    true
}
else {
    println("a is odd")
    false
}




val someVar = 2

if (someVar % 2 ==0 ) {
    println("It is an even Number")
}
else if (someVar % 2 != 0) {
    println("It is an Odd Number")
}
else {
    println("Don't know what that number is to be honest")
}

if (someVar < 0) {
    println("It is a negative Number")
}
else {
    println("It is a positive Number")
}



// Create array


val someIntArray = Array(5) { i -> i}
someIntArray.toList()


val someStringArray = Array(5) {i -> "$i"}
someStringArray.toList()

someStringArray[2] = "some"
someStringArray[3] = "some"
someStringArray.toList()

someStringArray.contains("some")


// Unmodifiable lists

val unmodifiableList = listOf<Any>(1, 2, 3, 4, 5)
unmodifiableList.contains(3)


// Modifiable Lists

val modifiableList = ArrayList<Any>()
modifiableList.add(1)
modifiableList.add(2)
modifiableList.add(3)
modifiableList.add(4)
modifiableList.add(5)
modifiableList.add("some")
modifiableList
modifiableList.last { i -> i == "some" }
modifiableList.indexOf("some")
modifiableList.remove(2)
modifiableList
modifiableList.dropLast(2)


// HashSets  Collection Of unordered same type data

val someSet = HashSet<Int>(10)
someSet.add(1)
someSet.add(3)
someSet.add(2)
someSet.add(4)
someSet.add(7)
someSet.add(6)
someSet.add(5)
someSet

someSet.remove(1)
someSet



// HashMaps Key-Value pairs



val someHashMap = HashMap<Int, Any>()

someHashMap[1] = "one"
someHashMap[2] = "two"
someHashMap[3] = "three"
someHashMap
someHashMap.size

// This is some conditional statements Flow controls

if (5 in someHashMap.keys) {
    println("Yes Baby")
}
else if (10 in someHashMap.keys) {
    println("Oh Yeah Baby")
}
else {
    println("None Of The Above")
}

