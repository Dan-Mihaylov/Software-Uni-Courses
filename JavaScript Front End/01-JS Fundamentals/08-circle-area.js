function solve(num) {
    const numType = typeof(num);
    let result;

    if (numType === 'number') {
        result = Math.pow(num, 2) * Math.PI;
        result = result.toFixed(2);
    } else {
        result = `We can not calculate the circle area, because we receive a ${numType}.`
    };

    console.log(result);
};


function solveTwo(num) {
    console.log(typeof(num) === 'number'? (Math.pow(num, 2) * Math.PI).toFixed(2) : `We can not calculate the circle area, because we receive a ${typeof(num)}.` )
};


solveTwo(5);
solveTwo('some string');