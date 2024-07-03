function solve (sentence, word) {

    const resultArray = sentence.split(' ');

    const counter = resultArray
    .filter(w => w === word)
    .length;
    console.log(counter);
};

solve('This is a word and it also is a sentence',
'is');
solve('softuni is great place for learning new programming languages',
'softuni');


function solution2(sentence, word){
    const occurance = sentence.match(new RegExp(`\\b${word}\\b`, 'g'));
    console.log(
        occurance ? occurance.length : 0
    );
};

solution2('This is a word and it also is a sentence',
    'is');
solution2('softuni is great place for learning new programming languages',
    'softuni');