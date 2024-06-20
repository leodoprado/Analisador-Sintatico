function clearValue() {
    document.getElementById("sentencesInput").value = '';
    document.getElementById("table").innerHTML = '';
}

document.addEventListener('DOMContentLoaded', function() {
    var rows = document.querySelectorAll('.table-row');
    rows.forEach(function(row, index) {
        row.style.display = 'none'; // Oculta a linha inicialmente
        setTimeout(function() {
            row.style.display = 'table-row'; // Exibe a linha após o intervalo
        }, index * 1000);
    });
});



