window.onpopstate = function(event) {
    console.log(event.state.section);
    showSection(event.state.section);
}

/*function showPage(page) {
    console.log("From showPage: " + page);
    
    document.querySelectorAll('section').forEach(section => {
        section.style.display = 'none';
    });
    document.querySelector(`#${page}`).style.display = "block";
};*/

function showSection(section) {
    console.log("showSection function: " + section);
    document.querySelectorAll('.navButton, .contentButton').forEach(button => {
        var classes = ['active']
        if (section === button.dataset.section) {
            button.classList.add(classes)
        } else {
            button.classList.remove(classes)
        }
    })

    fetch(`sections/${section}`)
    .then(response => response.text())
    .then(text => {
        document.querySelector('#content').innerHTML = text;    
        console.log("End of showSection.");
        updateState();
    });
};

function updateState() {
    document.querySelectorAll('.navButton, .contentButton').forEach(button => {
        button.onclick = function() {
            console.log("From onclick: " + this.dataset.section);
            const section = this.dataset.section;
            history.pushState({section: section}, "", `${section}`);

            //showPage(this.dataset.section);
            showSection(this.dataset.section);
            
        }
    })
}

document.addEventListener("DOMContentLoaded", function() {
    console.log("ContentLoaded");
    updateState();
})
