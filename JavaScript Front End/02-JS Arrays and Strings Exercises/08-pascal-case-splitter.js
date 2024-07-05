function pascalCaseSplitter(word:string) {
    const splitWords = word.match(/[A-Z][a-z]*/g);
    console.log(splitWords.join(', '))
};

pascalCaseSplitter('SplitMeIfYouCanHaHaYouCantOrYouCan');
pascalCaseSplitter('ThisIsSoAnnoyingToDo');