function extractSpices(spices) {
    let daysWorked = 0;
    let totalSpice = 0;
    const workersConsumption = 26;

    while (spices >= 100) {
        totalSpice += Math.max(spices - workersConsumption, 0);
        daysWorked += 1;
        spices -= 10;
    };

    totalSpice = Math.max(totalSpice - workersConsumption, 0);
    console.log(daysWorked);
    console.log(totalSpice);
};

extractSpices(111);
extractSpices(450);
