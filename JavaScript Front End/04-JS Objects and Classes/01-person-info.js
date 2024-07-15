function personInfo(...args){
    const info = {
        'firstName': args[0],
        'lastName': args[1],
        'age': args[2],
    };

    return info;
};


console.log(personInfo('Peter', 'Pan', 20));
console.log(personInfo('George', 'Smith', 18));
