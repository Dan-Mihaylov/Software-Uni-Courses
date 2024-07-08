function formatGrade(grade){
    if (grade < 3.00){
        console.log(`Fail (${2})`);
    } else if (3 <= grade && grade < 3.5) {
        console.log(`Poor (${grade.toFixed(2)})`);
    } else if (3.50 <= grade && grade < 4.50) {
        console.log(`Good (${grade.toFixed(2)})`);
    } else if (4.50 <= grade && grade < 5.50) {
        console.log(`Very good (${grade.toFixed(2)})`);
    } else if ( 5.50 <= grade) {
        console.log(`Excellent (${grade.toFixed(2)})`)
    };
};

formatGrade(3.33);
formatGrade(4.50);
formatGrade(2.99);