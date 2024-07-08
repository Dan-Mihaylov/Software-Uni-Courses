function repeatString(str, times){
    let result = (a, b) => a.repeat(b);
    console.log(result(str, times)); 
};

// repeatString('abc', 3);
// repeatString('String', 2);

function repeatRecursive(str, times, n=1) {
    if (n == times){
        return str;
    };
    return str + repeatRecursive(str, times, n+1);
}

console.log(repeatRecursive('abc', 3));
console.log(repeatRecursive('String', 2));
