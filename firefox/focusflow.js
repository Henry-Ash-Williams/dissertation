const getVisibleTextElements = require("getTextElements");

console.log(`[+] FocusFlow loaded!`);

getVisibleTextElements(elements => {
  console.log(elements)
});

