// let name = prompt("enter your name: ");

console.log("running js");

alert("dumnmy warning")

const doc = document.getElementsByClassName("count")

console.log(doc)

// const createPage = (req, res) = {

// }

let tutorials = [
    {
     url: "dark.jpg",
     description: "- send command /special_link<br>click the create button dummy js",
     count: 3
    },
    {
    url: "tutorial2.jpg",
    description: "- after send the message you want to store to bot dium,mmyt description more to text uint",
    count: 4
    },
    {
     url: "tutorial3.jpg",
     description: "- if you want to store more mssage then send messages one by one to bot.",
     count: 5
    }
];

function createPage(){
    
    const doc = document.getElementById("tutoriald");
    // for (const fruit of fruits){...}
    for(let i = 0; i< tutorials.length; i++){
        const div = document.createElement("div")
        div.className = "tutorials";
        div.innerHTML = `
             <img class="tutorial-img" src="${tutorials[i]['url']}" alt="tutorial 1 image">
             <p class="count">${tutorials[i]["count"]}</p>
             <p class="description">${tutorials[i]['description']}</p>
        `
        doc.appendChild(div)
        
    }
}

createPage()