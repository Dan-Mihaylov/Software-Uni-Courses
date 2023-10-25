fun checkLength(password: String): Boolean {
    return password.length in 6..10
}

fun containsLettersAndDigitsOnly(password: String): Boolean {
    return password.all { it.isLetterOrDigit() }
}

fun containsAtLeastTwoDigits(password: String): Boolean {
    var count = 0
    for (char in password) {
        if (char.isDigit()) {
            count++
        }
    }
    return count >= 2
}

fun passwordValidator() {
    println("######   Enter a Valid Password:                                       ######")
    println("######   A valid password must contain: Only Alphanumeric characters   ######")
    println("######   Be Between 6 and 10 characters (Inclusive)                    ######")
    println("######   Contain at least 2 digits                                     ######")
    val userPassword = readln()
    val errorMessages = ArrayList<String>()

    if (!containsLettersAndDigitsOnly(userPassword)) {
        val message = "Password Does Not Contain Letters and Digits Only!"
        errorMessages.add(message)
    }
    if (!checkLength(userPassword)) {
        val message = "Password Is Not The Right Length"
        errorMessages.add(message)
    }
    if (!containsAtLeastTwoDigits(userPassword)) {
        val message = "Password Must Contain At Least 2 Digits."
        errorMessages.add(message)
    }

    if (errorMessages.isEmpty()) {
        println("You have successfully chosen a password.")
    } else {
        println(errorMessages.joinToString("\n"))
    }
}

passwordValidator()
