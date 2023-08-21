function getElementsInViewport() {
  const elementsInViewport = [];

  const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting && !elementsInViewport.includes(entry.target)) {
        elementsInViewport.push(entry.target);
      }
    });
  }, {
    root: null,
    rootMargin: '0px',
    threshold: 0, 
  });

  document.querySelectorAll('*').forEach(element => {
    observer.observe(element);
  });

  return elementsInViewport;
}

function filterElements(elements) {
  const textElems = elements.filter(element => element.nodeType === Node.TEXT_NODE);

  return textElems;
}

function getVisibleTextElements(callback) {
  const elements = getElementsInViewport(); 

  callback(elements);
}

function logScrollEvents() {
  getVisibleTextElements(elements => console.log(`${elements.length} elements currently in the viewport`));
}

document.onload = function() {
  console.log("Focus-Flow V0.1 Loaded");
  document.addEventListener("scroll", logScrollEvents);
  console.log("Event logger registered");
}