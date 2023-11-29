function updateVisibleElements(elements: NodeListOf<Element>, callback: Function): void {
    const visibleElements = [];
    elements.forEach((element: Element) => {
        if (isElementPartiallyInViewport(element)) {
            visibleElements.push(element);
        }
    }); 

    visibleElements.forEach((element: Element) => {
        callback(element);
    });
}

// Test if a given element is within the viewport 
function isElementPartiallyInViewport(element: Element): boolean {
    const rect: DOMRect = element.getBoundingClientRect();
    const windowHeight: number = window.innerHeight || document.documentElement.clientHeight;
    const windowWidth: number = window.innerWidth || document.documentElement.clientWidth;
 
    const vertInView: boolean = (rect.top <= windowHeight) && ((rect.top + rect.height) >= 0);
    const horInView: boolean = (rect.left <= windowWidth) && ((rect.left + rect.width) >= 0);
 
    return vertInView && horInView;
} 

export default updateVisibleElements;