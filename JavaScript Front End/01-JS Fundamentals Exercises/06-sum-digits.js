function solve(number) {
    let result = 0;

    while (number > 0) {
        result = result + number % 10;
        number = Math.floor(number / 10);
    };

    console.log(result);
};

solve(245678);
