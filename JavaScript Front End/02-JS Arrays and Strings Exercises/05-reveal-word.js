function revealWord(words, sentence) {
    const wordsSplit = words.split(', ');

    for (const word of wordsSplit) {
        const n = word.length;
        const lookFor = ''.padEnd(n, '*');
        sentence = sentence.replace(lookFor, word);
    };

    console.log(sentence);
};


revealWord('great', 'softuni is ***** place for learning new programming languages');
revealWord('great, learning', 'softuni is ***** place for ******** new programming languages');
