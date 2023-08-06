function getElementsInViewport() {
  const elementsInViewport = [];

  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting && !elementsInViewport.includes(entry.target)) {
        elementsInViewport.push(entry.target);
      }
    });
  }, {
    root: null,
    rootMargin: '0px',
    threshold: 0.1, // Adjust this threshold as needed
  });

  document.querySelectorAll('*').forEach((element) => {
    observer.observe(element);
  });

  return elementsInViewport;
}

function filterElements() {
  const acceptedTags = ["p", "h1", "h2", "h3", "h4", "h5", "h6", "article", "aside", "b", "em", "footer", "header", "li", "s", "section", "small", "strong"];
  const visibleElems = getElementsInViewport(); 
  
  const textElems = visibleElems.filter(element => {
    return acceptedTags.includes(element.nodeName.toLowerCase());
  }); 

  return textElems;
}

function getVisibleTextElements(callback) {
  const elements = filterElements(); 

  callback(elements);
}

export { getVisibleTextElements };
