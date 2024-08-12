function attachEvents() {
  const baseUrl =  'http://localhost:3030/jsonstore/collections/students';
  const tableBodyEl = document.querySelector('tbody');
  
  document.onload = loadStudents();
  document.getElementById('submit').addEventListener('click', createEntry);
  
  async function loadStudents(){
    tableBodyEl.innerHTML = '';
    
    try {
      const response = await fetch(baseUrl);
      const responseData = await response.json();
      Object.values(responseData).forEach(value => createRow(value));
    } catch (error) {
      console.error('Some Error Ocurred', error);
    }
  }
  
  function createRow(data) {
    const trElement = document.createElement('tr');
    
    const tdFirstNameElement = document.createElement('td');
    tdFirstNameElement.textContent = data.firstName;
    
    const tdLastNameElement = document.createElement('td');
    tdLastNameElement.textContent = data.lastName;
    
    const tdFacNumElement = document.createElement('td');
    tdFacNumElement.textContent = data.facultyNumber;
    
    const tdGradeElement = document.createElement('td');
    tdGradeElement.textContent = data.grade;
    
    trElement.append(tdFirstNameElement, tdLastNameElement, tdFacNumElement, tdGradeElement);
    tableBodyEl.append(trElement);
  }
  
  async function createEntry(event) {
    const [firstNameEl, lastNameEl, facultyNumberEl, gradeEl] = document.querySelectorAll('input[type="text"]');
    
    if (!firstNameEl.value || !lastNameEl.value || !facultyNumberEl.value || !gradeEl.value) {
      return;
    }
    
    const newDataObject = {
      firstName: firstNameEl.value,
      lastName: lastNameEl.value,
      facultyNumber: facultyNumberEl.value,
      grade: gradeEl.value
    }

    options = {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(newDataObject)
    }

    try {
      const response = await fetch(baseUrl, options);
      if (!response.ok) {
        throw Error('Error creating new Entry');
      }
      loadStudents();
    } catch (error) {
      console.error('Something went wrong!', error);
    }
    
    firstNameEl.value = '';
    lastNameEl.value = '';
    facultyNumberEl.value = '';
    gradeEl.value = '';
  }
}

attachEvents();
