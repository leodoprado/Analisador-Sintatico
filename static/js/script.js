function clearValue() {
    document.getElementById("sentencesInput").value = '';
    document.getElementById("table").innerHTML = '';
}

document.addEventListener('DOMContentLoaded', function() {
    var form = document.getElementById('my-form');

    form.addEventListener('submit', function(event) {
        var stepByStepButton = document.getElementById('delayed-button');
        
        // Check if the step-by-step button was clicked
        if (event.submitter === stepByStepButton) {
            // Add a flag to indicate step-by-step mode
            var hiddenField = document.createElement("input");
            hiddenField.type = "hidden";
            hiddenField.name = "step_by_step";
            hiddenField.value = "true";
            form.appendChild(hiddenField);
        }
    });

    // Check if we need to display rows step-by-step
    if (document.getElementById('step-by-step-flag')) {
        var rows = document.querySelectorAll('.table-row');
        rows.forEach(function(row, index) {
            row.style.display = 'none'; // Hide the row initially
            setTimeout(function() {
                row.style.display = 'table-row'; // Show the row after the interval
            }, index * 1000);
        });
    }
});
