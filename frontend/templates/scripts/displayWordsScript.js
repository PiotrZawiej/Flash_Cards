import { createDeleteButton } from "./delateWord.js";

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
        wordTitle.className = "wordTitle";
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

        
        const deleteButton = createDeleteButton(wordItem, wordObj);

        wordItem.appendChild(wordTitle);
        wordItem.appendChild(deleteButton);

        wordList.appendChild(wordItem);
    });
}

fetchWords();
