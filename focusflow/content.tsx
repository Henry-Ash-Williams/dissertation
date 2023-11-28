import React from "react";

const styles = {
    container: {
      width: 300,
      height: 300,
      margin: "50px",
      backgroundColor: "#F38BA8",
      display: "flex",
      flexDirection: "column",
      justifyContent: "center",
      alignItems: "center",
      color: "#11111B",
      borderRadius: 10,
      fontFamily: "sans-serif",
    } as React.CSSProperties,
  };

const UiElement = () => {
  return <p style={styles.container}>Hello<br />FocusFlow!</p>;
}

// export default UiElement;