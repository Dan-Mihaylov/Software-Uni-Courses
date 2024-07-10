function charactersInRange(charOne, charTwo){
    const rangeValueOne = charOne.charCodeAt();
    const rangeValueTwo = charTwo.charCodeAt();

    let result = [];

    if (rangeValueOne < rangeValueTwo){
        for (let i = rangeValueOne + 1; i < rangeValueTwo; i++){
            result.push(String.fromCharCode(i));
        };
    } else {
        for (let i = rangeValueTwo + 1; i < rangeValueOne; i++) {
            result.push(String.fromCharCode(i));
        };
    };

    return result.join(' ');
};

console.log(charactersInRange('a', 'd'));
console.log(charactersInRange('#', ':'));
console.log(charactersInRange('C', '#'));



// console.log(String.fromCharCode(97));
// console.log('a'.charCodeAt());
// console.log(typeof('a'.charCodeAt()));