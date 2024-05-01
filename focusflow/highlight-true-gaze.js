function attachClickEventToParagraphs() {
    /* 
     * Attaches an event listener waiting for click events to 
     * every paragraph element on the page. Once an element is 
     * clicked, display a blue border around it with the text 
     * "true gaze location" above it. When another paragraph element is 
     * clicked, remove the blue border from every paragraph with 
     * the existing blue border. 
     */ 

    function removeCustomStyling() {
        const elementsWithBorder = document.querySelectorAll('.true-gaze-location');
        elementsWithBorder.forEach(function(element) {
            element.classList.remove('true-gaze-location');
        });
    }

    const paragraphs = document.getElementsByTagName('p');
  
    for (let i = 0; i < paragraphs.length; i++) {
        paragraphs[i].addEventListener('click', function() {
            removeCustomStyling();
        
            this.classList.add('true-gaze-location');
        });
    }
}
  
const trueGazeStyleElement = document.createElement('style');
const trueGazeStyleRule = `
.true-gaze-location {
    border: 2px solid blue; 
}

.true-gaze-location::before {
    content: "Location of true gaze"; 
    position: absolute;
    top: -20px; 
    left: 0;
}
`;
trueGazeStyleElement.innerText = trueGazeStyleRule; 
document.head.appendChild(trueGazeStyleElement);
attachClickEventToParagraphs();