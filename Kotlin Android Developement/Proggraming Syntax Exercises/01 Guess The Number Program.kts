import java.util.Random


fun guessTheNumber(){
    val randomInt = Random().nextInt(100)
    var attempts = 0

    while (true){
        attempts++
        println("Guess the Number:")
        val userInput = readLine()

        try {
            userInput?.toInt()

        } catch (e: Exception){
            println("You have entered an Invalid User Input.")
            return
        }

        val formattedUserInput = userInput?.toInt()
        if (randomInt == formattedUserInput) {
            println("You have guessed the number: $randomInt in $attempts tries.")
            return
        } else if (randomInt < formattedUserInput!!) {
            println("Your number is higher than the random number.")
        } else {
            println("Your number is lower than the random number.")
        }
    }
}