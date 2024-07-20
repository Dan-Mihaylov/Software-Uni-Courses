function wordsTracker(wordsArray){

    const wordsCounter = Object.fromEntries(
        wordsArray.shift()
        .split(' ')
        .map(word => [word, 0])
    );

    for (const word of wordsArray) {
        if (wordsCounter.hasOwnProperty(word)){
            wordsCounter[word] += 1;
        }
    }

    const sortedCounter = Object.entries(
        wordsCounter
    ).sort((a, b) => b[1] - a[1])

    sortedCounter.forEach(
        array => {
            console.log(`${array[0]} - ${array[1]}`);
        }
    )

}

wordsTracker(
    [
        'this sentence', 
        'In', 'this', 'sentence', 'you', 'have', 'to', 'count', 'the', 'occurrences', 'of', 'the', 'words', 'this', 'and', 'sentence', 'because', 'this', 'is', 'your', 'task'
        ]
);

wordsTracker(
    [
        'is the', 
        'first', 'sentence', 'Here', 'is', 'another', 'the', 'And', 'finally', 'the', 'the', 'sentence']
);

