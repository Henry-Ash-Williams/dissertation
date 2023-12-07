import React from "react";
const style = {
  container: {
    width: 100, 
    height: 100, 
    background: "red"
  }
}
const UiElement = () => {
  return <div className="injected-by-focus-flow"></div>;
}

export default UiElement;