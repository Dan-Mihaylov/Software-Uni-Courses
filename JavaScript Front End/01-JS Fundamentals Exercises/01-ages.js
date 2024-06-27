function solve(number) {
    if (0 <= number && number <= 2){
        console.log('baby');
    } else if (3 <= number && number <= 13) {
        console.log('child');
    } else if ( 14 <= number && number <= 19) {
        console.log('teenager');
    } else if (20 <= number && number <= 65) {
        console.log('adult');
    } else if (number >= 66) {
        console.log('elder');
    } else {
        console.log('out of bounds');
    };
};

solve(20);
solve(1);
solve(100);
solve(-1);