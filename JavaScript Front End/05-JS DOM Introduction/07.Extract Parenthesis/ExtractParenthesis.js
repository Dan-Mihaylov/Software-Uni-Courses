function extract(content) {
    const regex = /\(([\w\s]+)\)/g;
    const contentElement = document.getElementById('content');

    const matches = contentElement
        .textContent
        .match(regex)
        .map((match) => match.slice(1, match.length - 1));

    return matches.join('; ');
}