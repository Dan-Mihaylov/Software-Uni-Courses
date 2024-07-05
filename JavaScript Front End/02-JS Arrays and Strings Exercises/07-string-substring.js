function stringSubstring(str, sentence) {
    const lowercaseSentence = sentence.split(' ').map((word) => word.toLowerCase());
    const lowercaseString = str.toLowerCase();

    if (lowercaseSentence.indexOf(lowercaseString) > -1) {
        console.log(str);
    } else {
        console.log(`${str} not found!`);
    };
};

stringSubstring('javascript', 'JavaScript is the best programming language');
stringSubstring('python', 'JavaScript is the best programming language');