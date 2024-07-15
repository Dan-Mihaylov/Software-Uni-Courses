function convert(jsonString){
    const obj = JSON.parse(jsonString);

    for (const key in obj){
        console.log(`${key}: ${obj[key]}`);
    };
};


convert('{"name": "George", "age": 40, "town": "Sofia"}');
convert('{"name": "Peter", "age": 35, "town": "Plovdiv"}');


// JSON.parse()  --> To convert a text string into an JS object
// JSON.stringify() --> To convert a JS object into a text string