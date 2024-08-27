document.getElementById('register-form').addEventListener('submit', async function(event) {
    event.preventDefault();

    const email = document.getElementById('email').value;
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    const birth_date = document.getElementById('birth_date').value;

    try {
        const response = await fetch('http://localhost:8000/register', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ email, username, password, birth_date })  // Konwersja danych na JSON
        });

        if (response.ok) {
            const result = await response.json();
            alert(result.message);  // Pokazanie wiadomości zwróconej przez serwer
        } else {
            const error = await response.json();
            alert(`Error: ${error.detail}`);
        }
    } catch (error) {
        alert('An unexpected error occurred.');
    }
});
