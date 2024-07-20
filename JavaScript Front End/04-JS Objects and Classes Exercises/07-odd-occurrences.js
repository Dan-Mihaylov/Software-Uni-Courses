function oddOccurrences(str) {

    const counter = new Object();

    str.split(' ').forEach(
        el => {
            el = el.toLowerCase();
            if (counter[el]) {
                counter[el] += 1;
            } else {
                counter[el] = 1;
            }
        }
    )
    const result = new Array();

    for (const key in counter) {
        if (counter[key] % 2 != 0) {
            result.push(key);
        }
    }

    return result.join(' ');

}

console.log(oddOccurrences('Java C# Php PHP Java PhP 3 C# 3 1 5 C#'));
console.log(oddOccurrences('Cake IS SWEET is Soft CAKE sweet Food'));