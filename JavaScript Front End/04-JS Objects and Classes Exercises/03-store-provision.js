function storeProvisions(...provisionsArray){
    const provisions = new Object();

    function fillProvisions(provArray){
        for (let i = 0; i < provArray.length; i+=2) {
            const product = provArray[i];
            const quantity = parseInt(provArray[i + 1]);

            if (!provisions[product]) {
                provisions[product] = quantity;
            } else {
                provisions[product] += quantity;
            }
        }
    }

    provisionsArray.forEach(arr => {fillProvisions(arr)});
    const entries = Object
    .entries(provisions)
    .forEach(entry => {
        let product;
        let quantity;

        [product, quantity] = entry;
        console.log(`${product} -> ${quantity}`);
    })

}

storeProvisions(
    [
        'Chips', '5', 'CocaCola', '9', 'Bananas', '14', 'Pasta', '4', 'Beer', '2'
        ],
        [
        'Flour', '44', 'Oil', '12', 'Pasta', '7', 'Tomatoes', '70', 'Bananas', '30'
        ]
        
);

storeProvisions(
    [
        'Salt', '2', 'Fanta', '4', 'Apple', '14', 'Water', '4', 'Juice', '5'
        ],
        [
        'Sugar', '44', 'Oil', '12', 'Apple', '7', 'Tomatoes', '7', 'Bananas', '30'
        ]
);
