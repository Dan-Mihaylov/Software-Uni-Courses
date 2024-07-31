function create(words) {

   const contentElement = document.getElementById('content');

   words.forEach(word=>{
      const divElement = document.createElement('div');
      const pElement = document.createElement('p');
      
      divElement.append(pElement);
      pElement.style.display = 'none';
      pElement.textContent = word;

      divElement.addEventListener('click', (e)=>{
         pElement.style.display = 'block';
      })

      contentElement.append(divElement);
   })

}