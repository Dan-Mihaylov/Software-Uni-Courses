function listOfNames(names){
    const sortedNames = names.toSorted((a, b) => a.localeCompare(b));
    
    for (i = 0; i < names.length; i++) {
        console.log(`${i + 1}.${sortedNames[i]}`)
    };
};


listOfNames(["John", "Bob", "Christina", "Ema"]);