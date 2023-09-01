document.addEventListener("DOMContentLoaded", function(event) { 
    var term = new Terminal({
        cols: 80,
        rows: 24
    });
    term.open(document.getElementById('terminal'));
    document.getElementsByClassName("xterm-helper-textarea")[0].focus();

function fetchData(searchType, searchValue) {
    fetch('/search?criteria=' + searchType + '&value=' + searchValue)
    .then(response => response.json())
    .then(data => {
        // Display data in the terminal or elsewhere
        term.writeln(JSON.stringify(data));
    });
}

term.onKey(e => {
    const ev = e.domEvent;
    const printable = !ev.altKey && !ev.ctrlKey && !ev.metaKey;
    
    if (ev.keyCode === 13) { // Enter key
        processInput(currentInput);  // A new function to process the input
        currentInput = '';  // Clear the input
    } else if (printable) {
        term.write(e.key);
        currentInput += e.key;  // Add the key to our input string
    }
});

var currentInput = '';

function processInput(input) {
    input = input.toUpperCase();
    switch(input) {
        case 'A':
            // Handle search by Car Make
            break;
        case 'B':
            // Handle search by Car Model
            break;
        // ... and so on for the other options
        default:
            term.writeln('Invalid option. Please try again.');
    }
}
});