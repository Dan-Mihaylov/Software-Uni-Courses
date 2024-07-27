function solve() {
   document.querySelector('#searchBtn').addEventListener('click', onClick);

   function onClick() {
      const searchElementValue = document.getElementById('searchField').value;
      const rowsElements = document.querySelectorAll('tbody tr');
      const rowsChildrenElements = [];

      for (const row of rowsElements) {
         row.className = '';
         rowsChildrenElements.push(row.children);
      }

      if (!searchElementValue) {
         return;
      }
      for (const childrenElements of rowsChildrenElements) {
         for (const child of childrenElements) {
            const textValue = child.textContent;
            if (textValue.includes(searchElementValue)) {
               child.parentNode.className = 'select';
            }
         }
      }

   }
}
