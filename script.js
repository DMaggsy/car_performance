var term = new Terminal({
    cols: 80,
    rows: 24
});
term.open(document.getElementById('terminal'));

function fetchData() {
    let searchType = document.getElementById('searchType').value;
    let searchValue = document.getElementById('searchValue').value;
    
    fetch('/search?criteria=' + searchType + '&value=' + searchValue)
    .then(response => response.json())
    .then(data => {
        // Display data in the terminal or elsewhere
        term.writeln(JSON.stringify(data));
    });
}
