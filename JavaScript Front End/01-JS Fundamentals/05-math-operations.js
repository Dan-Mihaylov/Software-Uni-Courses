function solve(firstNum, secondNum, operant){
    if (operant == '+') {
        console.log(firstNum + secondNum);
    } else if (operant == '-') {
        console.log(firstNum - secondNum);
    } else if (operant == '*') {
        console.log(firstNum * secondNum);
    } else if (operant == '/') {
        console.log(firstNum / secondNum);
    } else if (operant == '%') {
        console.log(firstNum % secondNum);
    } else if (operant == '**') {
        console.log(firstNum ** secondNum);
    };
};


solve(5, 6, '+');
solve(3, 5.5, '*');