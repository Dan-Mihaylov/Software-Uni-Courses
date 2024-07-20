function piccolo(parkingInfo) {
    const parking = new Set();
    
    for (let i = 0; i < parkingInfo.length; i++){
        let direction;
        let licensePlate;
        
        [direction, licensePlate] = parkingInfo[i].split(', ');
        
        if (direction === 'IN') {
            parking.add(licensePlate);
        } else if (direction === 'OUT') {
            parking.delete(licensePlate);
        }
    }
    
    const sortedParking = Array();
    parking.forEach(el => {sortedParking.push(el)});
    sortedParking.sort((a, b) => a.localeCompare(b));
    
    if (sortedParking.length > 0) {
        for (let key of sortedParking) {
            console.log(key);
        }
    } else {
        console.log('Parking Lot is Empty')
    }
}


piccolo(
    ['IN, CA2844AA',
        'IN, CA1234TA',
        'OUT, CA2844AA',
        'IN, CA9999TT',
        'IN, CA2866HI',
        'OUT, CA1234TA',
        'IN, CA2844AA',
        'OUT, CA2866HI',
        'IN, CA9876HH',
        'IN, CA2822UU']
    );
    
piccolo(
    ['IN, CA2844AA',
        'IN, CA1234TA',
        'OUT, CA2844AA',
        'OUT, CA1234TA']
);