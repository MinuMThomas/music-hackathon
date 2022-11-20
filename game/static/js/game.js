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

// Play music modified from Stack Overflow, details in README
var audio = document.getElementById('audioFile');
var playBtn = document.getElementById('playButton')

playBtn.addEventListener("click", function(){
    clearTimeout(timeOut);
    setTimeout(function(){
        audio.play();
        
        setTimeout(function(){
            audio.pause();
            audio.currentTime = 0;
        }, 2000);
    }, 1000);
})

