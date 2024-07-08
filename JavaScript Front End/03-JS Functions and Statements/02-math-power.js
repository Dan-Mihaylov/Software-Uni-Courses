function mathPower(number, power){
    console.log(number ** power);
};

mathPower(2, 8);
mathPower(3, 4);


function recursivePower(base, radix, n=0, result=1) {

    if (n == radix) {
        return result;
    };
    result *= base
    return recursivePower(base, radix, n + 1, result);
};

console.log(recursivePower(2, 8));
console.log(recursivePower(3, 4));