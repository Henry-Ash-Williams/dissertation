export {}


function updateStyles(textElems: NodeList): void {
    const visibleElements = [];
    textElems.forEach((element: Element) => {
        // element.style.border = isElementPartiallyInViewport(element) ? "1px solid blue" : "1px solid red";

        if (isElementPartiallyInViewport(element)) {
            visibleElements.push(element);
        }
    }); 

    console.group("visible titles: ");
    visibleElements.forEach((element: Element) => {
        try { 
            console.log(element.childNodes[4].childNodes[0].childNodes[0].innerHTML);
        } catch (e) {
            return ;
        }
    });
    console.groupEnd();
}


function isElementPartiallyInViewport(element: Element): boolean {
    // Special bonus for those using jQuery
    var rect = element.getBoundingClientRect();
    var windowHeight = window.innerHeight || document.documentElement.clientHeight;
    var windowWidth = window.innerWidth || document.documentElement.clientWidth;
 
    var vertInView = (rect.top <= windowHeight) && ((rect.top + rect.height) >= 0);
    var horInView = (rect.left <= windowWidth) && ((rect.left + rect.width) >= 0);
 
    return vertInView && horInView;
} 

console.log("FocusFlow Loaded!!");
const textElems = document.querySelectorAll('tr[class="athing"]');
document.addEventListener("scroll", _ => { updateStyles(textElems); } );