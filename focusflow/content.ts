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
        const visibilityState = getVisibilityState();

        if (visibilityState === "visible") {
            /* navigator.mediaDevices.getUserMedia({video: true})
                .then(stream => {
                    console.log(stream);

                })
                .catch(err => {

                });*/ 
            document.title = "Visible";
            console.log(`Hidden page, #${n++}`);
        } else {
            document.title = "Hidden";
            console.log(`Focused page, #${n++}`);
        }
    }

    // Set up the event listener for visibility change
    document.addEventListener('visibilitychange', handleVisibilityChange);

    // Initial check for visibility state
    handleVisibilityChange();
}