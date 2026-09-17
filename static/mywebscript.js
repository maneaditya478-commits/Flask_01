let RunSentimentAnalysis = () => {
    let textToAnalyze = document.getElementById("textToAnalyze").value;

    let responseDiv = document.getElementById("system_response");

    if (!textToAnalyze || textToAnalyze.trim() === "") {
        responseDiv.innerHTML = "Invalid text! Please try again!";
        responseDiv.className = "result-box error";
        return;
    }

    responseDiv.innerHTML = "Analyzing emotion, please wait...";
    responseDiv.className = "result-box loading";

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState === 4) {
            if (this.status === 200) {
                responseDiv.innerHTML = this.responseText;
                if (this.responseText.includes("Invalid text")) {
                    responseDiv.className = "result-box error";
                } else {
                    responseDiv.className = "result-box success";
                }
            } else {
                responseDiv.innerHTML = "An error occurred while connecting to the server. Please try again.";
                responseDiv.className = "result-box error";
            }
        }
    };
    xhttp.open("GET", "/emotionDetector?textToAnalyze=" + encodeURIComponent(textToAnalyze), true);
    xhttp.send();
};

let clearInput = () => {
    document.getElementById("textToAnalyze").value = "";
    let responseDiv = document.getElementById("system_response");
    responseDiv.innerHTML = "Results will appear here after analysis.";
    responseDiv.className = "result-box";
};
