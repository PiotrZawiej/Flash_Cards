async function fetchWords() {
    try {
        const response = await fetch('http://localhost:8000/learn_words');
        const words = await response.json();
        displayWords(words);
    } catch (error) {
        console.error('Error fetching words:', error);
    }
}

function displayWords(words) {
    const wordList = document.getElementById('wordList');
    wordList.innerHTML = '';  // Clear any existing content

    words.forEach(wordObj => {
        const wordItem = document.createElement('div');
        wordItem.className = 'word-item';

        const wordTitle = document.createElement('h3');
        wordTitle.textContent = wordObj.word;

        const wordDefinition = document.createElement('p');
        wordDefinition.textContent = wordObj.definition;

        wordItem.appendChild(wordTitle);
        wordItem.appendChild(wordDefinition);

        wordList.appendChild(wordItem);
    });
}

fetchWords();