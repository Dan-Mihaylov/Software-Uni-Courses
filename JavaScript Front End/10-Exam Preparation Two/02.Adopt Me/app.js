function solve() {
  
  const animalTypeInputEl = document.getElementById('type');
  const animalAgeInputEl = document.getElementById('age');
  const animalGenderOptionEl = document.getElementById('gender');

  const adoptionInfoEl = document.getElementById('adoption-info');
  const adoptedListEl = document.getElementById('adopted-list');

  const adoptBtnEl = document.getElementById('adopt-btn');
  adoptBtnEl.addEventListener('click', adoptPet);

  function adoptPet(event) {
    event.preventDefault();

    const typePet = animalTypeInputEl.value;
    const agePet = animalAgeInputEl.value;
    const genderPet = animalGenderOptionEl.value;

    if (!typePet || !agePet || !genderPet) {
      return;
    }
    clearInputs();
    addAdoptionInfo(typePet, agePet, genderPet);
  }

  function clearInputs() {
    animalTypeInputEl.value = '';
    animalAgeInputEl.value = '';
    animalGenderOptionEl.value = '';
  }

  function addAdoptionInfo(typePet, agePet, genderPet){
    const liEl = document.createElement('li');

    const articleEl = document.createElement('article');
    liEl.appendChild(articleEl);

    const typePetEl = document.createElement('p');
    typePetEl.textContent = `Pet:${typePet}`;
    articleEl.appendChild(typePetEl);

    const genderPetEl = document.createElement('p');
    genderPetEl.textContent = `Gender:${genderPet}`;
    articleEl.appendChild(genderPetEl);
    
    const agePetEl = document.createElement('p');
    agePetEl.textContent = `Age:${agePet}`;
    articleEl.appendChild(agePetEl);

    // div with buttons el
    const divEl = document.createElement('div');
    divEl.classList.add('buttons');
    liEl.appendChild(divEl);

    const buttonEditEl = document.createElement('button');
    buttonEditEl.classList.add('edit-btn');
    buttonEditEl.textContent = 'Edit';
    buttonEditEl.addEventListener('click', () => editPet(typePet, agePet, genderPet, liEl));
    divEl.appendChild(buttonEditEl);

    const buttonDoneEl = document.createElement('button');
    buttonDoneEl.classList.add('done-btn');
    buttonDoneEl.textContent = 'Done';
    buttonDoneEl.addEventListener('click', () => donePet(liEl));
    divEl.appendChild(buttonDoneEl);

    adoptionInfoEl.appendChild(liEl);
  }

  function editPet(typePet, agePet, genderPet, liEl) {
    liEl.remove();
    animalTypeInputEl.value = typePet;
    animalAgeInputEl.value = agePet;
    animalGenderOptionEl.value = genderPet;
  }

  function donePet(liEl) {
    const liClone = liEl.cloneNode(true);
    liEl.remove();

    liClone.children[1].remove();

    const buttonClearEl = document.createElement('button');
    buttonClearEl.classList.add('clear-btn');
    buttonClearEl.textContent = 'Clear';
    buttonClearEl.addEventListener('click', () => clearEntry(liClone));
    liClone.appendChild(buttonClearEl);

    adoptedListEl.appendChild(liClone);
  }

  function clearEntry(entryEl) {
    entryEl.remove();
  }

}
  

solve();