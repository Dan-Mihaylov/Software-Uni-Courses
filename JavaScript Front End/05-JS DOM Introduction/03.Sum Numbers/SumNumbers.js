function calc() {
    // TODO: sum = num1 + num2
    const num1 = document.getElementById('num1');
    const num2 = document.getElementById('num2');
    const sum = document.getElementById('sum');

    const result = Number(num1.value) + Number(num2.value);
    sum.value = result;
}
