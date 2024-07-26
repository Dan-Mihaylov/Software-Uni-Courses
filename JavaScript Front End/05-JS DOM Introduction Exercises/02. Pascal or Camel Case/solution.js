function solve() {

  const availableNamingConventions = {
    'Pascal Case': (textList) => {
      textList = textList.map((el)=>el[0].toUpperCase() + el.slice(1, el.length).toLowerCase());
      return textList.join('');
    },
    'Camel Case': (textList) => {
      const firstWord = textList[0].toLowerCase();
      const laterWords = textList
        .slice(1, textList.length)
        .map((el)=> el[0].toUpperCase() + el.slice(1, el.length).toLowerCase());
      const result = Array(firstWord, ...laterWords);
      return result.join('');
    }
  }

  const textElementValue = document.getElementById('text').value;
  const namingConventionElementValue = document.getElementById('naming-convention').value;
  const resultElement = document.getElementById('result');

  if (! availableNamingConventions.hasOwnProperty(namingConventionElementValue)){
    resultElement.textContent = 'Error!';
  } else {

    const textValuesList = textElementValue.split(' ');
    const result = availableNamingConventions[namingConventionElementValue](textValuesList);

    resultElement.textContent = result;
  }

}