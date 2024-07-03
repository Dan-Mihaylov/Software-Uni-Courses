function solve(array){
    let sumEven = 0;
    let sumOdd = 0;

    for (let number of array) {
        if (number % 2 == 0) {
            sumEven += number;
        } else {
            sumOdd += number;
        };
    };

    console.log(sumEven - sumOdd);
};

solve([1, 2, 3, 4, 5, 6]);
solve([3, 5, 7, 9]);
solve([2, 4, 6, 8, 10]);
