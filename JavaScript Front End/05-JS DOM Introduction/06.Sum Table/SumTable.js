function sumTable() {
    const prices = Array.from(document.querySelectorAll('tr:not(:last-child) td:nth-child(2)')).map((el)=>Number(el.textContent));
    const sumElement = document.getElementById('sum');

    let result = 0;

    for (const price of prices){
        result += price;
    }

    sumElement.textContent = result;
}