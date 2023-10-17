document.getElementById("generateButton").addEventListener("click", function () {
    const description = document.getElementById("description").value;

    fetch("/generate", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ description }),
    })
        .then((response) => response.json())
        .then((data) => {
            document.getElementById("titleResult").textContent = data.title;
            document.getElementById("descriptionResult").textContent = data.description;
            document.getElementById("hashtagsResult").textContent = data.hashtags;
        })
        .catch((error) => console.error(error));
});