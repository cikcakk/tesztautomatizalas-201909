window.onload = function() {
    document.getElementById("calculate-button").onclick = function() {
        let a = parseInt(document.getElementById("a-input").value);
        let b = parseInt(document.getElementById("b-input").value);

        let result = document.getElementById("result-div");

        result.innerHTML = a * b;
        return false;
    }
};