document.getElementById('wordForm').addEventListener('submit', async function(event) {
    event.preventDefault();  

    const word = document.getElementById('word').value;
    const definition = document.getElementById('definition').value;

    try {
        const response = await fetch('http://localhost:8000/lashcard/add_word', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ word, definition })
        });

        if (response.ok) {
            const result = await response.json();
            alert(result.message);

            document.getElementById('word').value = '';
            document.getElementById('definition').value = '';

            fetchWords();
        } else {
            const error = await response.json();
            alert(`Error: ${error.detail}`);
        }
    } catch (error) {
        alert('An unexpected error occurred.');
    }
});