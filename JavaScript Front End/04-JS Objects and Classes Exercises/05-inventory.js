function inventory(infoArray){

    const heroList = [];

    infoArray.forEach(info => {
        let heroName;
        let heroLvl;
        let heroItems;

        [heroName, heroLvl, heroItems] = info.split(' / ');

        heroList.push(
            new Object({Hero: heroName, level: parseInt(heroLvl), items: heroItems})
        );
    })

    heroList.sort(
        (a, b) => a.level - b.level
    ).forEach(heroInfo => {
        for (let key in heroInfo){
            key === 'Hero' ? console.log(`${key}: ${heroInfo[key]}`) : console.log(`${key} => ${heroInfo[key]}`);
        }
    })
}

inventory(
    [
        'Isacc / 25 / Apple, GravityGun',
        'Derek / 12 / BarrelVest, DestructionSword',
        'Hes / 1 / Desolator, Sentinel, Antara'
        ]
);

inventory(
    [
        'Batman / 2 / Banana, Gun',
        'Superman / 18 / Sword',
        'Poppy / 28 / Sentinel, Antara'
        ]
);
