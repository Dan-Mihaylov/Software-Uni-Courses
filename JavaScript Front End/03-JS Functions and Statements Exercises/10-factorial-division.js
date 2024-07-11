function factorialDivision(numOne, numTwo){

    function factorial(number){
        if (number <= 1){
            return number;
        };

        return number * factorial(number - 1);
    };

    const factorialOne = factorial(numOne);
    const factorialTwo = factorial(numTwo);
    const result = factorialOne / factorialTwo;

    return `${result.toFixed(2)}`;

};


console.log(factorialDivision(5, 2));
console.log(factorialDivision(6, 2));
