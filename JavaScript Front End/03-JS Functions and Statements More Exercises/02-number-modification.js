function numberModification(number){
    let numberString = number.toString();
    let lengthNumber = numberString.length;
    let sum = 0;

    for (let i = 0; i < lengthNumber; i++) {
        sum += Number.parseInt(numberString[i]);
    };

    if (sum / lengthNumber >= 5) {
        return number;
    };

    while (sum / lengthNumber < 5){
        numberString += '9';
        sum += 9;
        lengthNumber++;
    };

    return Number.parseInt(numberString);

};

console.log(numberModification(101));
console.log(numberModification(5835));
