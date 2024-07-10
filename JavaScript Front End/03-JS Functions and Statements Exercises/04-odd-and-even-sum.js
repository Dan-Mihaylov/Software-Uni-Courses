function oddEvenSum(number) {
    let evenSum = 0;
    let oddSum = 0;

    while (number > 0) {
        const currNumber = number % 10;

        if (currNumber % 2 === 0){
            evenSum += currNumber;
        } else {
            oddSum += currNumber;
        };

        number = Math.floor(number / 10);
    };

    return `Odd sum = ${oddSum}, Even sum = ${evenSum}`;

};

console.log(oddEvenSum(1000435));
console.log(oddEvenSum(3495892137259234));
