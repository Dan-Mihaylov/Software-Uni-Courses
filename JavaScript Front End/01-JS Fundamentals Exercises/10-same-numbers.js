function solve(number) {

    let isSame = true;
    let totalSum = 0;
    let previous;

    while (number > 0) {
        let current = number % 10;
        if (previous) {
            if (previous != current) {
                isSame = false;
            };
        } else {
            previous = current;
        };
        totalSum = totalSum + current;
        number = Math.floor(number / 10);
    };
    
    console.log(isSame);
    console.log(totalSum);
};

solve(2222222);
solve(1234);