function calculate(numOne, numTwo, operator){
    let result;
    switch(operator) {
        case 'multiply':
            result =(a, b) => a * b;
            break;
        case 'divide':
            result = (a, b) => a / b;
            break;
        case 'add':
            result = (a, b) => a + b;
            break;
        case 'subtract':
            result = (a, b) => a - b;
            break;
    };
    return result(numOne, numTwo)
};

console.log(calculate(5, 5, 'multiply'));
console.log(calculate(40, 8, 'divide'));
console.log(calculate(12, 19, 'add'));
console.log(calculate(50, 13, 'subtract'));

function calculateAsObject(numOne, numTwo, operator){
    const operations = {
        'multiply': (a, b) => a * b,
        'divide': (a, b) => a / b,
        'add': (a, b) => a + b,
        'subtract': (a, b) => a - b,
    };

    return operations[operator](numOne, numTwo);
};

console.log(calculateAsObject(5, 5, 'multiply'));
console.log(calculateAsObject(40, 8, 'divide'));
console.log(calculateAsObject(12, 19, 'add'));
console.log(calculateAsObject(50, 13, 'subtract'));
