function solve() {
  const outputElement = document.getElementById('output');
  const inputElement = document.getElementById('input');
  const inputList = inputElement.value.split('.').filter(Boolean).map((x)=>x.trim());
  const outputList = [];

  function createParagraph(text){
    const newElement = document.createElement('p');
    newElement.textContent = text + '.';
    outputElement.append(newElement);
  }

  for (let i = 0; i < inputList.length; i += 3) {
    const text = inputList.slice(i, i+3).join('. ');
    outputList.push(text);
  }

  outputList.forEach(text => {
    createParagraph(text);
  })

}
