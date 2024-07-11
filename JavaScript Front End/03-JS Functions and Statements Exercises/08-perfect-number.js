function isPerfectNumber(number){
    const notPerfectMessage = "It's not so perfect."
    const perfectNumberMessage = "We have a perfect number!"

    if (number < 0 || !Number.isInteger(number)) {
        console.log(notPerfectMessage);
        return;
    };

    const halfNumber = number / 2;
    const divisors = [];

    for (let currNumber = 1; currNumber <= halfNumber; currNumber++) {
        if (number % currNumber == 0) {
            divisors.push(currNumber);
        };
    };

    const sumNumbers = divisors.reduce((a, b) => a + b, 0);
    
    return sumNumbers === number ? perfectNumberMessage : notPerfectMessage;
};

console.log(isPerfectNumber(28));
console.log(isPerfectNumber(6));