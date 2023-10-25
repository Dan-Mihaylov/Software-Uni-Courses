fun wordAnalysis(){
    val vowelsList = listOf('a', 'e', 'o', 'u', 'i')
    println("Enter a word you would like to analyse:")
    val userInput = readLine()
    var countVowels = 0
    var countConsonants = 0
    val hashMap = HashMap <Char, Int>()

    if (userInput?.length!! == 0) {
        println("You haven't entered a valid input")
        return
    }

    for (char in userInput) {
        if (char in vowelsList) {
            countVowels++
        } else {
            countConsonants++
        }
        hashMap[char] = hashMap.getOrDefault(char, 0) + 1
    }
    println("You have \"$countVowels\" vowels\nYou have \"$countConsonants\" consonants.")
    val sortedHashMap = hashMap.entries.sortedByDescending { it.value }
    for ((letter, digit) in sortedHashMap){
        println("Letter: $letter, Count: $digit")
    }
}

wordAnalysis()



