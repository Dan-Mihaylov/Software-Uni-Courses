function palindromeIntegers(numbers){

    function isPalindrome(numberString){
        let reversed = '';
        for (i = numberString.length -1; i>=0; i--){
            reversed += numberString[i];
        };
        return reversed === numberString;
    };

    for (number of numbers) {
        const numberAsString = number.toString();
        console.log(isPalindrome(numberAsString));
    };

};

palindromeIntegers([123,323,421,121]);
palindromeIntegers([32,2,232,1010]);

// let num = 15;
// let text = num.toString();
// console.log(text);
// console.log(typeof(text));
