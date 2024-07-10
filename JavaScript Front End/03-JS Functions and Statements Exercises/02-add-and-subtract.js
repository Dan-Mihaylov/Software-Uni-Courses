function addAndSubtract(...args){
    
    const sum = (a, b) => a + b;
    const subtract = (a, b) => a - b;

    const resultSum = sum(args[0], args[1]);
    const resultSubtract = subtract(resultSum, args[2]);

    return resultSubtract;

};

console.log(addAndSubtract(23, 6, 10));
console.log(addAndSubtract(1, 17, 30));
console.log(addAndSubtract(42, 58, 100));
