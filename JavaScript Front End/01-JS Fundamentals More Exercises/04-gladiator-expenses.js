function findExpenses(lostFightsCount, helmetPrice, swordPrice, shieldPrice, armorPrice) {
    let replacedHelmets = 0;
    let replacedSwords = 0;
    let replacedShields = 0;
    let replacedArmors = 0;
    
    for (i = 1; i <= lostFightsCount; i++) {
        
        if (i % 2 == 0 && i % 3 == 0) {
            replacedHelmets += 1;
            replacedSwords += 1;
            replacedShields += 1;
            if (replacedShields % 2 == 0) {
                replacedArmors += 1
            };
        } else if (i % 2 == 0) {
            replacedHelmets += 1;
        } else if (i % 3 == 0) {
            replacedSwords += 1;
        };
    };
    
    let totalPrice = (helmetPrice * replacedHelmets) + (swordPrice * replacedSwords) + (shieldPrice * replacedShields) + (armorPrice * replacedArmors);
    
    console.log(`Gladiator expenses: ${totalPrice.toFixed(2)} aureus`);
    
};

findExpenses(7,2,3,4,5);
findExpenses(23,12.50,21.50,40,200);