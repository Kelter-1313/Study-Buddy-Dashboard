const text = document.querySelector("#textBox");
const zButton = document.querySelector("#zButton");
const pomoButton = document.querySelector("#pomoButton");
const studyButton = document.querySelector("#studyButton");

const ZoomBox = document.querySelector(".ZoomBox");
const pomoBox = document.querySelector(".pomoBox");
const studyBox = document.querySelector(".studyBox");

console.log();

zButton.addEventListener("click", (e) => {
    e.preventDefault();
    text.style="display:none";
    pomoBox.style="display:none";
    studyBox.style="display:none";
    ZoomBox.style="";
});

pomoButton.addEventListener("click", (e) => {
    e.preventDefault();
    text.style="display:none";
    ZoomBox.style="display:none";
    studyBox.style="display:none";
    pomoBox.style="";
});

studyButton.addEventListener("click", (e) => {
    e.preventDefault();
    text.style="display:none";
    pomoBox.style="display:none";
    ZoomBox.style="display:none";
    studyBox.style="";
});