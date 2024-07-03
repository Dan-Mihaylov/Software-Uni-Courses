function censor(sentence, word) {

    const censoredWord = sentence.replaceAll(word, '*'.repeat(word.length));
    console.log(censoredWord);
};

censor('A small sentence with some words', 'small');
censor('Find the hidden word', 'hidden');
