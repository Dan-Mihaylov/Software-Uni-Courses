function generateMatrix(size){
    let matrix = [];

    for (let i = 0; i < size; i++) {
        let currRow = [];

        for (let j = 0; j < size; j++) {
            currRow.push(size);
        };

        matrix.push(currRow);
    };

    for (row of matrix) {
        console.log(row.join(' '));
    };
};

generateMatrix(3);
generateMatrix(7);
generateMatrix(2);