function solution(word){
    const pattern = /[\d]+/;
    const matches = word.match(pattern);

    let numbers = [];

    for (let match of matches) {
        const parsed = parseInt(match);

        if (!parsed in numbers) {
            numbers.push(parsed);
        };

    };

    return numbers.length;

};

console.log("a123bc34d8ef34");
console.log("leet1234code234");
console.log("a1b01c001");
