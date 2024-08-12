function solution() {
    
    const baseUrl = 'http://localhost:3030/jsonstore/advanced/articles/list/ ';
    const detailsUrl = 'http://localhost:3030/jsonstore/advanced/articles/details/';
    const mainEl = document.getElementById('main');

    document.onload = loadArticles();
    
    // get all the article titles and create the elements
    async function loadArticles() {
        const response = await fetch(baseUrl);
        const responseData = await response.json();
        console.log(responseData);
        
        Object.values(responseData).forEach(article =>  createArticle(article));
        
    }
    
    async function createArticle(article) {
        
        const accordionDivEl = document.createElement('div');
        accordionDivEl.classList.add('accordion');
        
        const headDivEl = document.createElement('div');
        headDivEl.classList.add('head');
        accordionDivEl.appendChild(headDivEl);
        
        const spanTitleEl = document.createElement('span');
        spanTitleEl.textContent = article.title;
        headDivEl.appendChild(spanTitleEl);
        
        const buttonEl = document.createElement('button');
        buttonEl.classList.add('button');
        buttonEl.textContent = 'More';
        buttonEl.setAttribute('id', article._id);
        buttonEl.addEventListener('click', toggleArticle);
        headDivEl.appendChild(buttonEl);
        
        try {
            const articleDetailsResponse = await fetch(detailsUrl + article._id);
            const articleDetails = await articleDetailsResponse.json();
            const extraDivEl = document.createElement('div');
            extraDivEl.classList.add('extra');
            accordionDivEl.appendChild(extraDivEl);
    
            const pEl = document.createElement('p');
            pEl.textContent = articleDetails.content;
            extraDivEl.appendChild(pEl);
        } catch (error) {
            console.error(error);
        }

        mainEl.appendChild(accordionDivEl);
    }
    
    // on click less, remove the div

    function toggleArticle(event) {
        console.log('clicked');
        const extraDivEl = event.target.parentNode.parentNode.querySelector('.extra');
        console.log(extraDivEl);
        const text = event.target.textContent;
        console.log(text.toLowerCase());

        text.toLowerCase() == 'more' ? extraDivEl.style.display = 'block' : extraDivEl.style.display = 'none';
        text.toLowerCase() == 'more' ? event.target.textContent = 'Less' : event.target.textContent = 'More'
    }
    
}

solution();

