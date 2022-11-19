// Shows clues when button clicked
var clueOneBtn = document.getElementById('clueOneButton');
var clueOne = document.getElementById('clueOne');

clueOneBtn.addEventListener("click", function(){
    clueOne.classList.remove("hide");
})

var clueTwoBtn = document.getElementById('clueTwoButton');
var clueTwo = document.getElementById('clueTwo');

clueTwoBtn.addEventListener("click", function(){
    clueTwo.classList.remove("hide");
})