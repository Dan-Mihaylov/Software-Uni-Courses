function recursive(operation){
    switch(operation){
        case 'power':
        return function power(number, cycles) {
            if (cycles == 1) {
                return number
            };
            return number * power(number, cycles - 1);
        }; 
        break;
        
        case 'addition':
        return function multiply(number, cycles) {
            if (cycles == 1) {
                return number;
            };
            
            return number + add(number, cycles - 1);
        };
        break;
    };
};

console.log(recursive('power')(2, 8));
console.log(recursive('addition')(2, 8));
