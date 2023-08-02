function getMarkupInViewport(callback) {
  function isVisible(element, viewport) {
    // Determines if a given element is visible (within the viewport)
    let rect = element.getBoundingClientRect(); 
    let x1, x2, y1, y2; 

    x1 = rect.left; 
    x2 = x1 + element.offsetWidth;
    y1 = rect.top; 
    y2 = y1 + element.offsetHeight; 

    return !(x1 >= viewport.w || y1 >= viewport.h || x2 < 0 || y2 < 0);
  }

  function Viewport() {
    // Creates a new object with coordinates of the corners of the viewport 
    // and its width and height 
    this.x1 = window.pageXOffset; 
    this.w = window.innerWidth; 
    this.x2 = this.x1 + this.w - 1;
    this.y1 = window.pageYOffset; 
    this.h = window.innerHeight; 
    this.y2 = this.y1 + this.h - 1;
    return this; 
  }

  function onWindowScroll() {
    const viewport = new Viewport(); 

    for (let i = 0; i < document.body.childNodes.length; i++) 
      if (isVisible(document.body.childNodes[i], viewport))
        visible.push(document.body.childNodes[i]);


    return visible;
  }

  let visible = []; 

  addEventListener("scroll", _ => { 
    visible = [];
    let visibleElems = onWindowScroll();
    visible = visibleElems;
  }, false);

  callback(visible);
}
