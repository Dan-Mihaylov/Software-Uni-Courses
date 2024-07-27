function generateReport() {
    const result = [];
    const outputArea = document.getElementById('output');

    const checkedColumns = Array.from(document.querySelectorAll('thead tr th'))
    .map((el, i)=> el.children[0].checked ? [el.children[0].name, i] : [el.children[0].name, -1])
    .filter(el=>el[1] != -1);

    const bodyRowsElement = Array.from(document.querySelectorAll('tbody tr'))
    .forEach(row=>{
        const newObject = {};

        for (let [colName, index] of checkedColumns) {
            newObject[colName] = row.children[index].textContent;
        }
        
        result.push(newObject);
    });

    outputArea.value = JSON.stringify(result);     
}

// function generateReport() {
//     const selectedCols = Array.from(document.querySelectorAll('th input'))
//       .map((col, index) => col.checked ? index : -1)
//       .filter(index => index !== -1);

//       console.log(selectedCols);
  
//     const reportList = Array.from(document.querySelectorAll('tbody tr')).map(row => {
//       return selectedCols.reduce((acc, colIndex) => {
//         acc[document.querySelectorAll('th input')[colIndex].name] = row.cells[colIndex].textContent;
//         return acc;
//       }, {});
//     });
  
//     document.getElementById('output').value = JSON.stringify(reportList);
//   }