function solve() {
    const selectMenuToElement = document.getElementById('selectMenuTo')
    
    const toOptions = ['binary', 'hexadecimal'].forEach(
        option => {
            const newOption = document.createElement('option');
            newOption.value = option;
            newOption.textContent = option;
            selectMenuToElement.append(newOption);
        }
    );

    document.querySelector('#container button')
    .addEventListener('click', (event) =>{
        const num = Number(document.getElementById('input').value);
        const optionValue = document.getElementById('selectMenuTo').value;

        const result = optionValue === 'hexadecimal' ? num.toString(16).toUpperCase() : num.toString(2);

        const resultElement = document.getElementById('result');
        resultElement.value = result;        
    })
    
}