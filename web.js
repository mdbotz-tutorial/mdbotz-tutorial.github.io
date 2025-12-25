
let tutorials = [
    {
        url: "dark.jpg",
        description: "send command /special_link<br>click the create button dummy js"
    },
    {
        url: "tutorial2.jpg",
        description: "After send the message you want to store to bot dium,mmyt description more to text uint"
    },
    {
        url: "tutorial3.jpg",
        description: "If you want to store more mssage then send messages one by one to bot."
    },
    {
         url: "tutorial4.jpg",
         description: "To generate shareable link click the button named generate link"
    }   
];

function createPage(){
    
    const doc = document.getElementById("tutoriald");
    // for (const fruit of fruits){...}
    for(let i = 0; i< tutorials.length; i++){
        const div = document.createElement("div")
        div.className = "tutorials";
        div.innerHTML = `
             <img class="tutorial-img" src="images/${tutorials[i]['url']}" alt="tutorial 1 image">
             <p class="count">${i+1}</p>
             <p class="description">${tutorials[i]['description']}</p>
        `
        doc.appendChild(div)
        
    }
}

createPage()