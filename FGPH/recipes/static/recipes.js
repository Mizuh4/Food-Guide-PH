window.onpopstate = function(event) {
    console.log(event.state.section);
    showSection(event.state.section);
}

function showPage(page) {
    console.log("From showPage: " + page);
    
    document.querySelectorAll('section').forEach(section => {
        section.style.display = 'none';
    });
    document.querySelector(`#${page}`).style.display = "block";
};


function showSection(section) {
    console.log("showSection function: " + section);

    fetch(`sections/${section}`)
    .then(response => response.text())
    .then(text => {
        document.querySelector('#content').innerHTML = text;
        console.log(text);
        console.log("End of showSection.");
    });
};

document.addEventListener("DOMContentLoaded", function() {
    document.querySelectorAll('button').forEach(button => {
        button.onclick = function() {
            console.log("From onclick: " + this.dataset.section);
            const section = this.dataset.section;
            history.pushState({section: section}, "", `${section}`);

            //showPage(this.dataset.section);
            showSection(this.dataset.section);
            
        }
    })
})