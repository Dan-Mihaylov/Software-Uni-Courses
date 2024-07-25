function editElement(element, toReplace, replacer) {
    const text = element.textContent;
    const matcher = new RegExp(toReplace, 'g');
    const replaced = text.replace(matcher, replacer);
    element.textContent = replaced;
}

