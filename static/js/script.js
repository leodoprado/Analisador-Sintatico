function clearValue() {
    document.getElementById("sentencesInput").value = '';
    document.getElementById("table").innerHTML = '';
}

function generateSentence() {
    clearValue();
    const sentences = [
        'badcc',
        'dbcbdcd',
        'dbcbdca',
        'babadbccc',
        'bababcdcaa',
        'bababcdcbccc'
    ];
    const randomSentence = sentences[Math.floor(Math.random() * sentences.length)];
    document.getElementById('sentencesInput').value = randomSentence;
}

document.addEventListener('DOMContentLoaded', function() {
    let form = document.getElementById('my-form');

    form.addEventListener('submit', function(event) {
        let stepByStepButton = document.getElementById('stepbystep-button');
        
        if (event.submitter === stepByStepButton) {
            let hiddenField = document.createElement("input");
            hiddenField.type = "hidden";
            hiddenField.name = "step_by_step";
            hiddenField.value = "true";
            form.appendChild(hiddenField);
        }
    });

    if (document.getElementById('step-by-step-flag')) {
        let rows = document.querySelectorAll('.table-row');
        rows.forEach(function(row, index) {
            row.style.display = 'none';
            setTimeout(function() {
                row.style.display = 'table-row';
            }, index * 1000);
        });
    }
});
