function employees(arr) {
    const employeeNumbers = new Object();

    arr.forEach(eName => {
        employeeNumbers[eName] = eName.length;
    })

    for (let key in employeeNumbers) {
        console.log(`Name: ${key} -- Personal Number: ${employeeNumbers[key]}`);
    }
}

employees([
    'Silas Butler',
    'Adnaan Buckley',
    'Juan Peterson',
    'Brendan Villarreal'
    ]);

employees([
    'Samuel Jackson',
    'Will Smith',
    'Bruce Willis',
    'Tom Holland'
    ]);