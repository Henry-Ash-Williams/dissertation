const getVisibleTextElements = require("getTextElements");
let scrollEvents = 0;

console.log(`[+] FocusFlow loaded!`);

getVisibleTextElements(elements => {
  console.group(`[+] Scroll Event #${scrollEvents}`);
  console.log(elements);
  console.groupEnd();
});

