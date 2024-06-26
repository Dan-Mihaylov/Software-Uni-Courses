function solve(a, b, c) {
    let result;
    if (a > b && a > c) {
        result = a;
    } else if (b > a && b > c) {
        result = b;
    } else if (c > a && c > b) {
        result = c;
    };
    
    console.log(`The largest number is ${result}.`);
};

function solveTwo(a, b, c) {
    let result = a;
    let array = [b, c];

    for (item of array) {
        if (item > result) {
            result = item;
        };
    };
    console.log(`The largest number is ${result}.`);
};  

function solveThree(a, b, c) {
    let result = Math.max(a, b, c);
    console.log(`The largest number is ${result}.`)
};


solve(5, -3, 16);
solve(-3, -5, -22.5);