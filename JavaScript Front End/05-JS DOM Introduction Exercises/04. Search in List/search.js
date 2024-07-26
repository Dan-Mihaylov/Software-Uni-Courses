function search() {
   const ulElement = document.getElementById('towns');
   const elementsArray = Array(ulElement.children);
   const searchElementValue = document.getElementById('searchText').value;
   const resultElement = document.getElementById('result');
   let matches = 0;

   // reset styles
   for (const element of elementsArray[0]) {
      element.style.textDecorationLine = 'none';
      element.style.fontWeight = 'normal';
   }

   for (const element of elementsArray[0]) {
      const elText = element.textContent;
      const search = searchElementValue;

      if (elText.includes(search)) {
         element.style.textDecorationLine = 'underline';
         element.style.fontWeight = 'bold';
         matches += 1;
      }
   }

   matches > 0 ? `${resultElement.textContent = matches + ' matches found'}` : '';


}
