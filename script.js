// Welcome Message
window.onload = function () {
    console.log("Welcome to Visual Studio Code Clone");
};

// Download Button
function downloadVSCode() {
    window.open("https://code.visualstudio.com/download", "_blank");
}

// Theme Toggle
function toggleTheme() {
    document.body.classList.toggle("light-theme");
}

// Scroll to Top
function scrollTopPage() {
    window.scrollTo({
        top: 0,
        behavior: "smooth"
    });
}

// Search
function searchPage() {
    let word = prompt("Enter text to search:");

    if (word == null || word == "") {
        return;
    }

    if (document.body.innerText.toLowerCase().includes(word.toLowerCase())) {
        alert("'" + word + "' found on this page.");
    } else {
        alert("'" + word + "' not found.");
    }
}

// Show Current Date and Time
function showTime() {
    let now = new Date();
    alert(now.toLocaleString());
}

// Welcome Alert
function welcome() {
    alert("Welcome to the VS Code Clone Website!");
}

function runDemo(){

    alert("Running Code...");

}