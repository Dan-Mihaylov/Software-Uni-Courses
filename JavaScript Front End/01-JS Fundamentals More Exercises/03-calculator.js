function calculator(a, operant, b) {
    const operations = {
        '+': a + b,
        '-': a - b,
        '/': a / b,
        '*': a * b,
    };

    const result = operations[operant];
    console.log(result.toFixed(2));

};

calculator(5, '+', 10);
calculator(25.5, '-', 3);