function hashtag(sentence){
    let words = sentence.split(' ');
    let result = [];
    for (let word of words) {
        if (word.startsWith('#') && word.length > 1) {
            let isOnlyLetters = true;
            for (let i = 1; i < word.length; i++) {                
                if (!(word[i].match(/[a-zA-Z]/i))) {
                    isOnlyLetters = false;
                    break;
                }
            }
            if (isOnlyLetters) {
                result.push(word.substring(1));
            }
        }
    }
    console.log(result.join('\n'));
};

hashtag('Nowadays everyone uses #sp#pd21-_ # to tag a #special word in #socialMedia');
hashtag('The symbol # is known #variously in English-speaking #regions as the #number sign');
