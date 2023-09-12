document.addEventListener("DOMContentLoaded", function (event) {
    let term = new Terminal({
        cols: 80,
        rows: 24
    });
    term.open(document.getElementById('terminal'));
    document.getElementsByClassName("xterm-helper-textarea")[0].focus();

    function fetchData(searchType, searchValue) {
        fetch('/search', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    criteria: searchType,
                    value: searchValue
                })
            })
            .then(response => {
                if (!response.ok) {
                    return response.text().then(text => {
                        term.writeln('Server Response: ' + text);
                        throw new Error(text);
                    });
                }
                return response.json();
            })
            .then(data => {
                // Display data in the terminal or elsewhere
                term.writeln(JSON.stringify(data));
            })
            .catch((error) => {
                term.writeln('Error fetching data: ' + error.message);
            });
    }


    term.onKey(e => {
        const ev = e.domEvent;
        const printable = !ev.altKey && !ev.ctrlKey && !ev.metaKey;

        if (ev.keyCode === 13) { // Enter key
            processInput(currentInput); // A new function to process the input
            currentInput = ''; // Clear the input
        } else if (printable) {
            term.write(e.key);
            currentInput += e.key; // Add the key to our input string
        }
    });

    let currentInput = '';
    let searchMode = ''; // To store the current search criteria

    function processInput(input) {
        input = input.toUpperCase();

        if (searchMode) {
            // If a searchMode has been set, process the value input
            fetchData(searchMode, input);
            searchMode = ''; // Reset search mode
            currentInput = ''; // Clear the input
            return;
        }

        switch (input) {
            case 'A':
                term.writeln('Please enter Car Make:');
                searchMode = 'make';
                break;
            case 'B':
                term.writeln('Please enter Car Model:');
                searchMode = 'model';
                break;
            case 'C':
                term.writeln('Please enter Car Year:');
                searchMode = 'year';
                break;
            case 'D':
                term.writeln('Please enter Engine Size:');
                searchMode = 'engineSize';
                break;
            case 'E':
                term.writeln('Please enter Horsepower:');
                searchMode = 'horsepower';
                break;
            case 'F':
                term.writeln('Please enter Torque:');
                searchMode = 'torque';
                break;
            case 'G':
                term.writeln('Please enter 0-60:');
                searchMode = '0-60 MPH Time';
                break;
            case 'H':
                term.writeln('Please enter Price:');
                searchMode = 'price';
                break;
            default:
                term.writeln('Invalid option. Please try again.');
                currentInput = ''; // Clear the input
        }
    }

});