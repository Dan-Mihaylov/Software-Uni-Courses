function solution(arr) {
    const MAX_BULLETS = 6;
    const MAX_HEALTH = 100;
    posse = {};
    
    const heroesCount = Number(arr.shift());
    
    // Heroes processing logic
    arr.slice(0, heroesCount).forEach(hero => {
        const [heroName, heroHP, heroBullets] = hero.split(' ');
        posse[heroName] = {'hp': Number(heroHP), 'bullets': Number(heroBullets)};
    });
    
    // Commands processing logic
    arr.slice(heroesCount, arr.length).forEach(command => {
        if (command.includes('FireShot')) {
            const [_, charName, targetName] = command.split(' - ');
            fireShot(charName, targetName);
        } else if (command.includes('TakeHit')) {
            
            const [_, charName, damage, attackerName] = command.split(' - ');
            takeHit(charName, Number(damage), attackerName);
            
        } else if (command.includes('Reload')) {
            const [_, charName] = command.split(' - ');
            reload(charName);
        } else if (command.includes('PatchUp')) {
            const [_, charName, amount] = command.split(' - ');
            patchUp(charName, Number(amount));
        } else if (command.includes('Ride')) {
            printInfo();
        }
    })
    
    
    
    
    function fireShot(attacker, victim) {
        const character = posse[attacker];
        if (character.bullets == 0) {
            console.log(`${attacker} doesn't have enough bullets to shoot at ${victim}!`)
            return;
        }
        
        character.bullets -= 1;
        console.log(`${attacker} has successfully hit ${victim} and now has ${character.bullets} bullets!`)
    }
    
    function takeHit(victim, damage, attacker) {
        const victimObj = posse[victim];
        
        if (victimObj.hp <= damage) {
            console.log(`${victim} was gunned down by ${attacker}!`)
            delete posse[victim];
            return;
        }
        
        victimObj.hp -= damage;
        console.log(`${victim} took a hit for ${damage} HP from ${attacker} and now has ${victimObj.hp} HP!`)
    }
    
    function reload(charName) {
        
        const character = posse[charName];
        
        if (character.bullets == MAX_BULLETS) {
            console.log(`${charName}'s pistol is fully loaded!`);
            return;
        }
        
        const bulletsReloaded = MAX_BULLETS - character.bullets;
        character.bullets = MAX_BULLETS;
        console.log(`${charName} reloaded ${bulletsReloaded} bullets!`)
    }
    
    function patchUp(charName, amount) {
        const character = posse[charName];
        
        if (character.hp == MAX_HEALTH) {
            console.log(`${charName} is in full health!`);
            return;
        }
        
        const newHealth = Math.min(MAX_HEALTH, character.hp + amount);
        const healedAmount = newHealth - character.hp;
        character.hp = newHealth;
        
        console.log(`${charName} patched up and recovered ${healedAmount} HP!`);
    }
    function printInfo() {
        Object.keys(posse).forEach(key => {
            console.log(`${key}\n HP: ${posse[key].hp}\n Bullets: ${posse[key].bullets}`);
        });
        return;
    }
}



solution(["2",
    "Gus 100 4",
    "Walt 100 5",
    "FireShot - Gus - Bandit",
    "TakeHit - Walt - 100 - Bandit",
    "Reload - Gus",
    "Ride Off Into Sunset"]);
    