function orders(item, times){
    let total = 0;
    
    switch (item) {
        case 'coffee':
            total = 1.50 * times;
            break;
        case 'water':
            total = 1.00 * times;
            break;
        case 'coke':
            total = 1.40 * times;
            break;
        case 'snacks':
            total = 2.00 * times;
            break;
    };

    console.log(total.toFixed(2));
};


orders('water', 5);
orders('coffee', 2);

