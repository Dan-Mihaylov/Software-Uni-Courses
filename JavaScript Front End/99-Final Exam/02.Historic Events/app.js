window.addEventListener("load", solve);

function solve() {
  const nameInputEl = document.getElementById('name');
  const timeInputEl = document.getElementById('time');
  const descInputEl = document.getElementById('description');

  const previewListEl = document.getElementById('preview-list');
  const archiveListEl = document.getElementById('archive-list');

  const addEventBtnEl = document.getElementById('add-btn');
  addEventBtnEl.addEventListener('click', addEvent);

  [nameInputEl, timeInputEl, descInputEl].forEach(el => {
    el.addEventListener('input', (e)=>{addEventBtnEl.removeAttribute('disabled')});
  });

  function addEvent(event) {
    event.preventDefault();

    const name = nameInputEl.value;
    const time = timeInputEl.value;
    const description = descInputEl.value;

    clearInputs();

    if (!name || !time || !description) {
      return;
    }

    createEvent(name, time, description);
    addEventBtnEl.setAttribute('disabled', 'disabled');

  }

  function clearInputs() {
    nameInputEl.value = '';
    timeInputEl.value = '';
    descInputEl.value = '';
  }

  function createEvent(name, time, description) {
    const liEl = document.createElement('li');

    const articleEl = document.createElement('article');
    liEl.appendChild(articleEl);

    const nameEl = document.createElement('p');
    nameEl.textContent = name;
    articleEl.appendChild(nameEl);

    const timeEl = document.createElement('p');
    timeEl.textContent = time;
    articleEl.appendChild(timeEl);

    const descEl = document.createElement('p');
    descEl.textContent = description;
    articleEl.appendChild(descEl);

    // buttons div
    const buttonsDivEl = document.createElement('div');
    buttonsDivEl.classList.add('buttons');
    liEl.appendChild(buttonsDivEl);

    const editBtnEl = document.createElement('button');
    editBtnEl.classList.add('edit-btn');
    editBtnEl.textContent = 'Edit';
    editBtnEl.addEventListener('click', () => editEntry(name, time, description, liEl));
    buttonsDivEl.appendChild(editBtnEl);

    const nextBtnEl = document.createElement('button');
    nextBtnEl.classList.add('next-btn');
    nextBtnEl.textContent = 'Next';
    nextBtnEl.addEventListener('click', () => nextFunctionality(liEl));
    buttonsDivEl.appendChild(nextBtnEl);

    // add liEl to preview
    previewListEl.appendChild(liEl);
  }

  function nextFunctionality(liEl) {
    liEl.remove();
    const buttonDivEl = liEl.children[1];
    buttonDivEl.remove();

    const archiveBtnEl = document.createElement('button');
    archiveBtnEl.classList.add('archive-btn');
    archiveBtnEl.textContent = 'Archive';
    archiveBtnEl.addEventListener('click', () => archiveEntry(liEl));
    liEl.appendChild(archiveBtnEl);

    archiveListEl.appendChild(liEl);
  }

  function archiveEntry(liEl) {
    liEl.remove();
    addEventBtnEl.removeAttribute('disabled');
  } 

  function editEntry(name, time, description, liEl) {
    addEventBtnEl.removeAttribute('disabled');
    nameInputEl.value = name;
    timeInputEl.value = time;
    descInputEl.value = description;
    liEl.remove();
  }
}