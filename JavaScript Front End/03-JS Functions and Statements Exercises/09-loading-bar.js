function loadingBar(percentage){

    let result = '';
    let bar = Array(10).fill('.');
    if (percentage === 100) {
        result = '100% Complete!\n[%%%%%%%%%%]';
    } else {
        for (let i = 0; i < percentage / 10; i++) {
            bar[i] = '%';
        };
        result = `${percentage}% [${bar.join('')}]\n`;
        result += 'Still loading...'
    };

    return result;
};

console.log(loadingBar(30));
console.log(loadingBar(50));
console.log(loadingBar(100));
