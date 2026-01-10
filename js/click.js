
function onClick(element) {
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
           dropBar.style.display = "flex";
        }
    })
}

function main() {
    let toggleBar = document.getElementsByClassName("crossbar")
    for (var i = 0; i < toggleBar.length; i++) {
        onClick(toggleBar[i])
    }
}


main()