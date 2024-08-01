function solve() {
  const [generateBtnElement, buyBtnElement] = document.querySelectorAll('button');
  
  generateBtnElement.addEventListener('click', generateItems);
  buyBtnElement.addEventListener('click', buyItems);
  
  function generateItems(event) {
    const textareaElement = document.querySelectorAll('textarea')[0];
    JSON.parse(textareaElement.value)
      .forEach(item=>{
        createRows(item.img, item.name, item.price, item.decFactor);
      });
  }
  
  function buyItems(event) {
    const boughtItems = {
      'names': [],
      'totalPrice': 0,
      'totalDecFactor': 0,
    }

    const checkedRows = Array.from(document.querySelectorAll('tbody tr'))
    .filter((row)=> {
      return row.children[4].children[0].checked === true;
    });

    checkedRows.forEach(row=>{

      const itemName = row.children[1].children[0].textContent;
      const itemPrice = Number(row.children[2].children[0].textContent);
      const itemDecFac = Number(row.children[3].children[0].textContent);

      boughtItems.names.push(itemName);
      boughtItems.totalPrice += itemPrice;
      boughtItems.totalDecFactor += itemDecFac;
    })
    
    visualizeBoughtItems(boughtItems);
  }

  function visualizeBoughtItems(boughtItems) {
    const resultAreaElement = document.querySelectorAll('textarea')[1];
    let result = '';

    result += `Bought furniture: ${boughtItems.names.join(', ')}`;
    result += `\nTotal price: ${boughtItems.totalPrice.toFixed(2)}`;
    result += `\nAverage decoration factor: ${boughtItems.totalDecFactor / boughtItems.names.length}`;

    resultAreaElement.value = result;
  }

  function createRows(itemImg, itemName, itemPrice, itemDecFactor) {
    const rowElement = document.createElement('tr');
    const imgDataElement = document.createElement('td');
    const imgElement = document.createElement('img');
    
    imgElement.setAttribute('src', itemImg);
    imgDataElement.append(imgElement);
    rowElement.append(imgDataElement);

    const itemNameDataElement = document.createElement('td');
    const itemNameElement = document.createElement('p');
    
    itemNameElement.textContent = itemName;
    itemNameDataElement.append(itemNameElement);
    rowElement.append(itemNameDataElement);

    const itemPriceDataElement = document.createElement('td');
    const itemPriceElement = document.createElement('p');

    itemPriceElement.textContent = itemPrice;
    itemPriceDataElement.append(itemPriceElement);
    rowElement.append(itemPriceDataElement);

    const itemDecFactorDataElement = document.createElement('td');
    const itemDecFactorElement = document.createElement('p');

    itemDecFactorElement.textContent = itemDecFactor;
    itemDecFactorDataElement.append(itemDecFactorElement);
    rowElement.append(itemDecFactorDataElement);

    const checkboxDataElement = document.createElement('td');
    const checkboxElement = document.createElement('input');

    checkboxElement.type = 'checkbox';
    checkboxDataElement.append(checkboxElement);
    rowElement.append(checkboxDataElement);

    addRowToTableBody(rowElement);
  }

  function addRowToTableBody(row) {
    const tableBody = document.querySelector('table tbody');
    tableBody.append(row);
  }
}