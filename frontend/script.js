let queryHistory = [];

async function performSearch(query = null) {
    const searchQuery = query != null ? query : document.getElementById("search-bar")?.value?.trim();

    console.log("Query parameter passed to function:", query);
    console.log("Value from search bar:", document.getElementById("search-bar")?.value);
    console.log("Final search query being sent:", searchQuery);

    if (!searchQuery) {
        alert("Please enter a search query.");
        return;
    }

    if (queryHistory.length === 0 || queryHistory[queryHistory.length - 1] !== searchQuery) {
        queryHistory.push(searchQuery);
    }

    console.log("Query history:", queryHistory);

    try {
        const response = await fetch (`http://127.0.0.1:5000/search?query=${encodeURIComponent(searchQuery)}`);
        if (!response.ok) {
            throw new Error(`Server error: ${response.status}`);
        }
        
        const data = await response.json();
        displayResults(data);
    } catch (error) {
        console.error("Error during search:", error);
        document.getElementById("results").innerHTML = `<p style="color:red;">An error occurred while searching. Please try again later.</p>`;
    }
}

function goBack() {
    if (queryHistory.length > 1) {
        queryHistory.pop(); 
        const previousQuery = queryHistory[queryHistory.length - 1];
        document.getElementById("search-bar").value = previousQuery; 
        performSearch(previousQuery); 
    } else {
        alert("No previous queries to go back to.");
    }
}

function displayResults(data) {
    const resultsDiv = document.getElementById("results");
    resultsDiv.innerHTML = "";

    const titleElement = document.createElement("h2");
    titleElement.innerText = data.title || "Search Result"; 
    resultsDiv.appendChild(titleElement);

    const summaryElement = document.createElement("p");
    summaryElement.innerText = data.answer || "No summary available.";
    resultsDiv.appendChild(summaryElement);

    const keywordContainer = document.createElement("div");
    keywordContainer.className = "keywords";

    data.keywords.forEach(keyword => {
        const span = document.createElement("span");
        span.innerText = keyword;
        span.className = "keyword";
        span.onclick = () => performSearch(keyword); 
        keywordContainer.appendChild(span);
    });

    resultsDiv.appendChild(keywordContainer);
}