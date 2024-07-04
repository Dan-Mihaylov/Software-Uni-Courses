function printWithStep(arr, step){
    let result = [];

    for (let i = 0; i < arr.length; i+=step) {
        result.push(arr[i]);
    };

    return result;
};


printWithStep(['5', '20', '31', '4', '20'], 2);
printWithStep(['dsa','asd', 'test', 'tset'], 2);
printWithStep(['1', '2','3', '4', '5'], 6);
