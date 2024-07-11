function showPage(page) {
    console.log("From showPage: " + page);
    
    document.querySelectorAll('section').forEach(section => {
        section.style.display = 'none';
    });
    document.querySelector(`#${page}`).style.display = "block";
};


function showSection(section) {
    console.log("showSection function ran");
    console.log(section);
    fetch(`${section}`)
    .then(response => response.text())
    .then(text => {
        console.log(section);
        document.querySelector('#content').innerHTML = text;
    });
};

document.addEventListener("DOMContentLoaded", function() {
    document.querySelectorAll('button').forEach(button => {
        button.onclick = function() {

            console.log("From onclick: " + this.dataset.section);
            //showSection(display);
            showPage(this.dataset.section);
            
        }
    })
})