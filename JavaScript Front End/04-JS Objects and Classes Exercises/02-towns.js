function towns(arr) {
    const result = new Array();
    const formattedArray = arr.map(el => el.split(' | '));

    formattedArray.forEach(arrElement => {
        let latitude = parseFloat(arrElement[1]).toFixed(2);
        let longitude = parseFloat(arrElement[2]).toFixed(2);
        const currObject = JSON.parse(
            `{"town": "${arrElement[0]}", "latitude": "${latitude}", "longitude": "${longitude}"}`
        )
        result.push(currObject);
    })

    for (let obj of result) {
        console.log(obj);
    }
}


towns(['Sofia | 42.696552 | 23.32601',
    'Beijing | 39.913818 | 116.363625']);