function wordsUppercase(words) {
    const allWords = words.match(/\w+/g);
    console.log(allWords.join(', ').toUpperCase());
};

wordsUppercase('Hi, how are you?');