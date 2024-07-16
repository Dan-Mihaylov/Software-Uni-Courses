function addressBook(infoArray){
    const infoArrayMapped = infoArray.map(el => el.split(':'));  
    const addresses = new Object();

    for(const info of infoArrayMapped){
        const personName = info[0];
        const address = info[1];

        addresses[personName] = address;
    };

    const entries = Object.entries(addresses);
    const entriesSorted = entries.sort(
        (a, b) => a[0].localeCompare(b[0])
    );

    for (const entry of entries) {
        console.log(entry[0] + ' -> ' + entry[1]);
    };
};


addressBook(['Tim:Doe Crossing','Bill:Nelson Place','Peter:Carlyle Ave','Bill:Ornery Rd']);
addressBook(['Bob:Huxley Rd','John:Milwaukee Crossing','Peter:Fordem Ave','Bob:Redwing Ave','George:Mesta Crossing','Ted:Gateway Way','Bill:Gateway Way','John:Grover Rd','Peter:Huxley Rd','Jeff:Gateway Way','Jeff:Huxley Rd'])

