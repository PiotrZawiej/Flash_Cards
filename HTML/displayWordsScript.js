async function fetchWords() {
    try {
        const response = await fetch('http://localhost:8000/learn_words');
        const words = await response.json();
        displayWords(words);
    } catch (error) {
        console.error('Error fetching words:', error);
    }
}


async function displayWords(words) {
    const wordList = document.getElementById('wordList');
    wordList.innerHTML = '';  // Clear any existing content

    words.forEach(wordObj => {
        const wordItem = document.createElement('div');
        wordItem.className = 'word-item';

        const wordTitle = document.createElement('h3');
        wordTitle.className = "wordTitle"
        wordTitle.textContent = wordObj.word;

        wordItem.addEventListener("click", function handleClick() {
            // Sprawdź, czy definicja już istnieje
            let existingDefinition = wordItem.querySelector('.definition');
            
            if (existingDefinition) {
                // Jeśli istnieje, usuń ją
                existingDefinition.remove();
            } else {
                // Jeśli nie istnieje, dodaj ją
                const wordDefinition = document.createElement('div');
                wordDefinition.className = 'definition'; // Dodajemy klasę, aby łatwo identyfikować definicję
                wordDefinition.innerHTML = wordObj.definition;
                wordItem.appendChild(wordDefinition);
            }
        });
        

        
        

        wordItem.appendChild(wordTitle);

        wordList.appendChild(wordItem);
    });
}

fetchWords();