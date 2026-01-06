console.log("dummy check")

// alert("checking")

function onClick(element) {
    console.log("log info")
    console.log(element)
    element.addEventListener('click', () => {
        let openBar = document.getElementById("openbar");
        let closeBar = document.getElementById("closebar");
        let dropBar = document.getElementById("bar");
        if (openBar.style.display == "none") {
           openBar.style.display = "block";
           closeBar.style.display = "none";
           dropBar.style.display = "none";
        } else {
           openBar.style.display = "none";
           closeBar.style.display = "block"; 
           dropBar.style.display = "block";
        }
    })
}
function hello() {
    // alert("nmae")
    let toggleBar = document.getElementsByClassName("crossbar")
    console.log(toggleBar)
    for (var i = 0; i < toggleBar.length; i++) {
        onClick(toggleBar[i])
        // alert(toggleBar[i])
    }
    
    // // toggleBar.innerHTML = `<div>dummy</div>`
    // toggleBar.addEventListener('click', () => {
    //       let hidden =  document.querySelector("div")
    //     //   hidden.classList.toggle("togglebar")
    //     //   alert("clicked")
    //       let bar = document.getElementById("bar")
    //     //   bar.style.display = "none";
    //       bar.classList.toggle("togglebar")
    //       let openBar = document.getElementById("openbar")
    //       openBar.style.display = "none";

    //       let closeBar = document.getElementById("closebar")
    //       closeBar.style.display = "block";
        //   alert(closeBar)
}


hello()