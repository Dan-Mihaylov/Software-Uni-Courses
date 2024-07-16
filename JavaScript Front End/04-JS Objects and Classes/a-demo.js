function iterate(){
    const arr = ['aa', 'bb', 'cc'];

    for (let el in arr){
        console.log(el);
    };
};

iterate();

function iterateAgain(){
    const obj = {
        'aa': 123,
        'bb': 234
    }

    for (let el in obj){
        console.log(el);
    };
};


iterateAgain();