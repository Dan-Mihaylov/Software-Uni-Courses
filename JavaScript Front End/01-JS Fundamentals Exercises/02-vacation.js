function vacation(groupSize, typeGroup, day) {
    let totalPrice;
    let price;
    let discount = 1;

    switch(typeGroup) {
        case 'Students':
            switch(day) {
                case 'Friday':
                    price = 8.45;
                    break;
                case 'Saturday':
                    price = 9.80;
                    break;
                case 'Sunday':
                    price = 10.46;
                    break;
            };
            if (groupSize >= 30) {
                discount = 0.85;
            };
            break;

        case 'Business':
            switch(day) {
                case 'Friday':
                    price = 10.90;
                    break;
                case 'Saturday':
                    price = 15.60;
                    break;
                case 'Sunday':
                    price = 16;
                    break; 
            };
            if (groupSize >= 100) {
                groupSize = groupSize - 10;
            };
            break;

        case 'Regular':
            switch(day) {
                case 'Friday':
                    price = 15;
                    break;
                case 'Saturday':
                    price = 20;
                    break;
                case 'Sunday':
                    price = 22.50;
                    break;
            };
            if (groupSize >= 10 && groupSize <= 20) {
                discount = 0.95;
            };
            break;

    };

    totalPrice = (price * groupSize) * discount;
    console.log(`Total price: ${totalPrice.toFixed(2)}`);
    
};

vacation(30, 'Students', 'Sunday');
vacation(40, 'Regular', 'Saturday');