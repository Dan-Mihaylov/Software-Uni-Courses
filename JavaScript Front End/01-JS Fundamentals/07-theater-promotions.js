function solve(type, age) {
    let result;

    switch(type) {
        case 'Weekday':
            if (0 <= age && age <= 18) {
                result = 12;
            } else if (18 < age && age <= 64) {
                result = 18;
            } else if (64 < age && age <= 122) {
                result = 12;
            };
            break;
        case 'Weekend':
            if (0 <= age && age <= 18) {
                result = 15;
            } else if (18 < age && age <= 64) {
                result = 20;
            } else if (64 < age && age <= 122) {
                result = 15;
            };
            break;
        case 'Holiday':
            if (0 <= age && age <= 18) {
                result = 5;
            } else if (18 < age && age <= 64) {
                result = 12;
            } else if (64 < age && age <= 122) {
                result = 10;
            };
            break;
    };

    if (result) {
        console.log(`${result}$`);
    } else {
        console.log('Error!');
    };
};


solve('Weekday', -2);
solve('Weekend', 12);
solve('Holiday', 18);