export {}

import updateVisibleElements from "~getVisibleElements";

console.log("FocusFlow Loaded 🎉 !!");

if (document.URL === "file:///Users/henrywilliams/Documents/uni/dissertation/focusflow/test.html") {
    console.log("Running in test environment");
    const textElems = document.querySelectorAll('.box');

    console.group("Visible elements");
    updateVisibleElements(textElems, element => {
        console.log(element.childNodes[0].innerHTML);
    }); 
    console.groupEnd();

    document.addEventListener("scroll", _ => {
        console.group("Visible elements");
        updateVisibleElements(textElems, element => {
            console.log(element.childNodes[0].innerHTML);
        }); 
        console.groupEnd();
    });
} else {
    let n: number = 0; 
    function getVisibilityState() {
        return document.visibilityState; 
    }
    // Function to handle visibility change
    function handleVisibilityChange() {
        // file deepcode ignore FunctionDeclarationInBlock: <please specify a reason of ignoring this>
        const visibilityState = getVisibilityState();

        if (visibilityState === "hidden") {
            console.log("Document no longer visible");
            let simulatedGazeLocation = (() => {
                const windowHeight: number = window.innerHeight || document.documentElement.clientHeight;
                const windowWidth: number = window.innerWidth || document.documentElement.clientWidth;
                return { 'x': Math.random() * windowWidth, 'y': Math.random() * windowHeight };
            })(); 
            console.log(simulatedGazeLocation)
            let paragraphs = document.querySelectorAll('p'); 

            updateVisibleElements(paragraphs, paragraph => {
                const bbox = paragraph.getBoundingClientRect(); 

                if (
                    simulatedGazeLocation.x >= bbox.left && 
                    simulatedGazeLocation.x <= bbox.right && 
                    simulatedGazeLocation.y >= bbox.top && 
                    simulatedGazeLocation.y <= bbox.bottom 
                ) {
                    paragraph.style.border = '2px solid red';
                }
            })
        } else if (visibilityState === "visible") {
            
        }
        
    }

    // Set up the event listener for visibility change
    document.addEventListener('visibilitychange', handleVisibilityChange);

    // Initial check for visibility state
    handleVisibilityChange();
}