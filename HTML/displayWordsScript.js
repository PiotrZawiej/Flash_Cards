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

        const deleteButton = document.createElement('button');
        

        const wordTitle = document.createElement('h3');
        wordTitle.className = "wordTitle"
        wordTitle.textContent = wordObj.word;

        wordItem.addEventListener("click", function handleClick() {
            let existingDefinition = wordItem.querySelector('.definition');
            
            if (existingDefinition) {
                existingDefinition.remove();
            } else {
                const wordDefinition = document.createElement('div');
                wordDefinition.className = 'definition'; 
                wordDefinition.innerHTML = wordObj.definition;
                wordItem.appendChild(wordDefinition);
            }
        });
        

        
        

        wordItem.appendChild(wordTitle);

        wordList.appendChild(wordItem);
    });
}

fetchWords();