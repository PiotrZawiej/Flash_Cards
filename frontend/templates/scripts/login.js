document.getElementById('login-form').addEventListener('submit', async function (event) {
    event.preventDefault();

    // Capture the values entered by the user
    const identifier = document.getElementById('email').value; // Either email or username
    const password = document.getElementById('password').value;

    try {
        // Send the login data to the backend
        const response = await fetch('http://localhost:8000/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ identifier, password }) 
        });

        
        if (response.ok) {
            const result = await response.json();
            alert('Login successful!');

            

            window.location.href = '/frontend/templates/mainPage.html'; 
        } else {
            // If the login failed, show an error message
            const errorData = await response.json();
            alert(`Login failed: ${errorData.detail}`);
        }
    } catch (error) {
        // Handle any errors that occurred during the fetch operation
        console.error('An error occurred:', error);
        alert('An unexpected error occurred. Please try again later.');
    }
});


