function substring(str, start, count){

    let result = "";
    let index = start;

    for (let i = 0; i <= count - start; i++) {
        result += str[index];
        index ++;
    };

    console.log(result);

};

substring('ASentence', 1, 8);
substring('SkipWord', 4, 7);
