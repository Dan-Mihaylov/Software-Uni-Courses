function solve(start, end) {
    let sum = 0;
    let result = '';

    for (i = start; i <= end; i++) {
        sum = sum + i;
        result = result + ' ' + i;
    };

    console.log(`${result.trimStart()}`)
    console.log(`Sum: ${sum}`)
};

solve(5, 10);
solve(0, 26);
solve(50, 60);