function signCheck(...args){
    const result = args.reduce(
        (a, b) => a * b
    );
    return result < 0 ? 'Negative' : 'Positive';
};

console.log(signCheck(5, 12, -15));
console.log(signCheck(-6, -12, 14));
console.log(signCheck(-1, -2, -3));
console.log(signCheck(-5, 1, 1));
