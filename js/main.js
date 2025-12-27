
export function createPage(arrays, elementID = "tutoriald"){
    
    const doc = document.getElementById(elementID);
    // for (const fruit of fruits){...}
    for(let i = 0; i< arrays.length; i++){
        const div = document.createElement("div")
        div.className = "tutorials";
        div.innerHTML = `
             <img class="tutorial-img" src="images/${arrays[i]['url']}" alt="tutorial 1 image">
             <p class="count">${i+1}</p>
             <p class="description">${arrays[i]['description']}</p>
        `
        doc.appendChild(div)
        
    }
}