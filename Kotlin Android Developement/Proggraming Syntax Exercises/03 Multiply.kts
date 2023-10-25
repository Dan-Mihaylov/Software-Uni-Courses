fun multiply(){
    println("Enter Your Digits In This Format: 1,2,3,4,5")
    val userArray = readln().split(",").map { it.toIntOrNull() }
    // Validating that input is only numbers.
    if (!userArray.all { it is Int }) {
        println("Invalid Input.")
        return
    }
    if (0 in userArray) {
        println("The result is: 0")
        // force unpack !!it because we are sure the program would have terminated if it was Null
    } else if (userArray.all { it!! > 0 }) {
        println("The result will be positive! +")
    } else {
        println("The result will be negative! -")
    }
    val result = userArray
        .map { it?.toInt() ?: 0 }
        .reduce { acc, i -> acc * i }
    println(result)
}

multiply()