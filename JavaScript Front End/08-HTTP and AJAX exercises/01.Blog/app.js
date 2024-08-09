function attachEvents() {
    const basePostsUrl = 'http://localhost:3030/jsonstore/blog/posts/';
    const baseCommentsUrl = 'http://localhost:3030/jsonstore/blog/comments/';
    const selectElement = document.getElementById('posts');
    const postTitleElement = document.getElementById('post-title');
    const postBodyElement = document.getElementById('post-body');
    const postCommentsElement = document.getElementById('post-comments');
    let allPosts;

    document.getElementById('btnLoadPosts').addEventListener('click', loadPosts);
    document.getElementById('btnViewPost').addEventListener('click', viewPost);

    async function viewPost(event) {
        const postId = selectElement.value;
        if (!postId){
            return;
        }

        const postData = allPosts.filter(post => post.id == postId)[0];

        const allCommentsResponse = await fetch(baseCommentsUrl);
        const allCommentsData = await allCommentsResponse.json();

        const postComments = Object.values(allCommentsData).filter(comment => comment.postId === postId);

        loadPostComments(postData, postComments);
    }

    function loadPostComments(postData, postComments) {
        // postTitleElement.innerHTML = '';
        // postBodyElement.innerHTML = '';
        postCommentsElement.innerHTML = '';

        const postBody = postData.body;
        const postTitle = postData.title;

        postTitleElement.textContent = postTitle;
        postBodyElement.textContent = postBody;

        postComments.forEach(commentData => {
            const liElement = document.createElement('li');
            // liElement.id = commentData[1].postId;
            liElement.textContent = commentData.text;
            postCommentsElement.append(liElement);
        })
    }

    async function loadPosts(event) {
        const response = await fetch(basePostsUrl);
        const data = await response.json();
        allPosts = Object.values(data);
        createOptionsElements(allPosts);
    }

    function createOptionsElements(optionsData) {
        selectElement.innerHTML = '';

        optionsData.forEach(data => {
            const optionsElement = document.createElement('option');
            optionsElement.value = data.id;
            optionsElement.textContent = data.title;
            selectElement.append(optionsElement);
        });
    }
}

attachEvents();
