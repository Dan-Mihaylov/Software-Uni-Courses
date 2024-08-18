function solve() {
  const nameInputEl = document.getElementById('name');
  const numberInputEl = document.getElementById('phone');
  const categoryInputEl = document.getElementById('category');

  document.getElementById('add-btn').addEventListener('click', submitInfo);

  function submitInfo(event) {
    event.preventDefault();
    const nameValue = nameInputEl.value;
    const numberValue = numberInputEl.value;
    const categoryValue = categoryInputEl.value;

    if (!nameValue.trim() || !numberValue.trim() || !categoryValue.trim()) {
      return;
    }

    clearFormValues();
    addPhoneNumber(nameValue, numberValue, categoryValue);
  }

  function clearFormValues(){
    nameInputEl.value = '';
    numberInputEl.value = '';
    categoryInputEl.value = '';
  }

  function addPhoneNumber(name, number, category) {
    const checklistElement = document.getElementById('check-list');

    const liEl = document.createElement('li');
    checklistElement.appendChild(liEl);

    const articleEl = document.createElement('article');
    liEl.appendChild(articleEl);

    const pNameEl =  document.createElement('p');
    pNameEl.textContent = `name:${name.trim()}`;
    articleEl.appendChild(pNameEl);

    const pPhoneEl = document.createElement('p');
    pPhoneEl.textContent = `phone:${number.trim()}`;
    articleEl.appendChild(pPhoneEl);

    const pCatEl = document.createElement('p');
    pCatEl.textContent = `category:${category.trim()}`;
    articleEl.appendChild(pCatEl);

    const divButtonsEl = document.createElement('div');
    divButtonsEl.classList.add('buttons');
    liEl.appendChild(divButtonsEl);

    const editButtonEl = document.createElement('button');
    editButtonEl.classList.add('edit-btn');
    editButtonEl.addEventListener('click', () => editEntry(liEl, name, number, category));
    divButtonsEl.appendChild(editButtonEl);

    const saveButtonEl = document.createElement('button');
    saveButtonEl.classList.add('save-btn');
    saveButtonEl.addEventListener('click', () => saveEntry(liEl));
    divButtonsEl.appendChild(saveButtonEl);

  }

  function editEntry(liElement, name, number, category) {
    liElement.remove();
    nameInputEl.value = name;
    numberInputEl.value = number;
    categoryInputEl.value = category;
  }

  function saveEntry(liElement) {
    const contactsListEl = document.getElementById('contact-list');

    const buttonsDivEl = liElement.querySelector('.buttons');
    buttonsDivEl.remove();

    const deleteButtonEl = document.createElement('button');
    deleteButtonEl.classList.add('del-btn');
    deleteButtonEl.addEventListener('click', () => {liElement.remove()});
  
    liElement.appendChild(deleteButtonEl);
    contactsListEl.appendChild(liElement);
    
  }
}
