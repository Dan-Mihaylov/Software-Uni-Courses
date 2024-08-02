function solve() {

    const values = '123';

    const [checkButtonElement, clearButtonElement] = document.querySelectorAll('tfoot button');

    checkButtonElement.addEventListener('click', checkValidity);
    clearButtonElement.addEventListener('click', clearTable);

    function checkValidity(e) {
        const tableElement = document.querySelector('table');
        const messageElement = document.querySelector('#check p');

        if (checkRows() && checkCols()) {
            tableElement.style.border = '2px solid green';
            messageElement.textContent = 'You solve it! Congratulations!'
        } else {
            tableElement.style.border = '2px solid red';
            messageElement.textContent = 'NOP! You are not done yet...'
        }
    }

    function checkRows(){
        const rows = Array.from(document.querySelectorAll('tbody tr'))
        .map((row) => [
            row.children[0].children[0].value,
            row.children[1].children[0].value, 
            row.children[2].children[0].value
        ]
        .sort((a, b) => a.localeCompare(b))
        .join('')
        );

        for (let el of rows) {
            if (el !== values) {
                return false;
            }
        }

        return true;
    }

    function checkCols(){
        const cols = [];
        const rowsElement = Array.from(document.querySelectorAll('tbody tr'));

        for (let i = 0; i < 3; i++) {
            let curr = [];
            
            rowsElement.forEach(row => {
                curr.push(row.children[i].children[0].value)
            })
        
            curr = curr.sort((a, b) => a.localeCompare(b)).join('');
            cols.push(curr);
        }

        for (let col of cols) {
            console.log(col);
            if (col !== values) {
                return false;
            }
        }

        return true;
    }

    function clearTable(e) {
        Array.from(document.querySelectorAll('tbody tr'))
            .forEach(row=>{
                Array.from(row.children).forEach(child=>{child.children[0].value = ''});
            });
        
        document.querySelector('table').style.border = 'none';
        document.querySelector('#check p').textContent = '';
    }
}
