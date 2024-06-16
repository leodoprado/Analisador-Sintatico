function confirmClearInput() {
    if (confirm("Deseja limpar o campo?")) {
        document.getElementById("sentencesInput").value = "";
    }
}