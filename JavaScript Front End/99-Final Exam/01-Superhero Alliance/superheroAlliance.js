function solve(arr) {
    const heroes = {}

    const numberSuperheroes = Number(arr[0]);
    const commands = arr.slice(numberSuperheroes + 1, arr.length - 1);
    
    arr.slice(1, numberSuperheroes + 1).forEach(heroInfo => {
        const [name, powers, energy] = heroInfo.split('-');
        
        heroes[name] = {
            'powers': powers.split(','),
            'energy': Number(energy)
        };
    });

    commands.forEach(commandInfo => {
        const [command, ...data] = commandInfo.split(' * ');
        
        switch (command) {
            case 'Use Power':
                usePower(...data);
                break;
            case 'Train':
                train(...data);
                break;
            case 'Learn':
                learn(...data);
                break;
        }
    })

    function usePower(heroName, powerName, energyRequired) {
        const hero = heroes[heroName];
        const energyNeeded = Number(energyRequired);
        
        if (hero.powers.includes(powerName) && hero.energy >= energyNeeded) {
            hero['energy'] -= energyNeeded;
            console.log(`${heroName} has used ${powerName} and now has ${hero.energy} energy!`);
            return;
        }

        console.log(`${heroName} is unable to use ${powerName} or lacks energy!`);
    }

    function train(heroName, trainEnergy) {
        const increaseEnergy = Number(trainEnergy);
        const hero = heroes[heroName];
        const currEnergy = hero.energy;

        if (currEnergy == 100) {
            console.log(`${heroName} is already at full energy!`);
            return;
        }

        hero.energy = Math.min(100, hero.energy + increaseEnergy);
        const energyGained = hero.energy - currEnergy;
        console.log(`${heroName} has trained and gained ${energyGained} energy!`);
    }

    function learn(heroName, newPower) {
        const hero = heroes[heroName];

        if (hero.powers.includes(newPower)) {
            console.log(`${heroName} already knows ${newPower}.`);
            return;
        }

        hero.powers.push(newPower);
        console.log(`${heroName} has learned ${newPower}!`);
    }

    Object.keys(heroes).forEach(hero => {
        const powers = heroes[hero]['powers'];
        console.log(`Superhero: ${hero}\n- Superpowers: ${powers.join(', ')}\n- Energy: ${heroes[hero]['energy']}`);
    });
}



solve([
        "2",
        "Iron Man-Repulsor Beams,Flight-100",
        "Thor-Lightning Strike,Hammer Throw-50",
        "Train * Thor * 20",
        "Learn * Thor * Hammer Throw",
        "Use Power * Iron Man * Repulsor Beams * 30",
        "Evil Defeated!"
    ])


