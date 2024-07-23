function pointsValidation(pointsArray) {
    let [x1, y1, x2, y2] = pointsArray;

    const firstCheck = Math.sqrt(x1 ** 2 + y1 ** 2);
    const secondCheck = Math.sqrt(x2 ** 2 + y2 ** 2);
    const thirdCheck = Math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2);

    console.log(`{${x1}, ${y1}} to {0, 0} is ${Number.isInteger(firstCheck) ? 'valid' : 'invalid'}`);
    console.log(`{${x2}, ${y2}} to {0, 0} is ${Number.isInteger(secondCheck) ? 'valid' : 'invalid'}`);
    console.log(`{${x1}, ${y1}} to {${x2}, ${y2}} is ${Number.isInteger(thirdCheck) ? 'valid' : 'invalid'}`);
};

pointsValidation([3, 0, 0, 4]);
pointsValidation([2, 1, 1, 1]);
