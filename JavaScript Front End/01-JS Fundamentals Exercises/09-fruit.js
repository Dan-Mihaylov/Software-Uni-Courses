function solve(fruit, grams, pricePerKilo) {
    const kilos = grams / 1000;
    const totalPrice = pricePerKilo * kilos;

    console.log(`I need $${totalPrice.toFixed(2)} to buy ${kilos.toFixed(2)} kilograms ${fruit}.`);
};


solve('orange', 2500, 1.80);
solve('apple', 1563, 2.35);