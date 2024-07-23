function carWash(actionsArray){

    let cleanPercentage = 0;

    const actions = {
        'soap': a => a + 10,
        'water': a => a * 1.2,
        'vacuum cleaner': a => a * 1.25,
        'mud': a => a * 0.9
    };

    for (let action of actionsArray) {
        cleanPercentage = actions[action](cleanPercentage);
    };

    return `The car is ${cleanPercentage.toFixed(2)}% clean.`

};

console.log(carWash(['soap', 'soap', 'vacuum cleaner', 'mud', 'soap', 'water']));
console.log(carWash(["soap", "water", "mud", "mud", "water", "mud", "vacuum cleaner"]));
