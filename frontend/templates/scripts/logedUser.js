document.addEventListener("DOMContentLoaded", async function() {
    try {
        // Wysłanie zapytania do serwera, aby sprawdzić, czy użytkownik jest zalogowany
        const response = await fetch('http://localhost:8000/check-auth', {
            method: 'GET',
            credentials: 'include'  
        });

        if (response.ok) {
            // Użytkownik jest zalogowany
            const userData = await response.json();
            console.log("Zalogowany użytkownik:", userData);

            document.getElementById("logout-button").style.display = "block";
            document.getElementById("login-button").style.display = "none";
            document.getElementById("register-button").style.display = "none";
        } else {
            // Użytkownik nie jest zalogowany
            document.getElementById("logout-button").style.display = "none";
            document.getElementById("login-button").style.display = "block";
            document.getElementById("register-button").style.display = "block";
        }
    } catch (error) {
        console.error('Wystąpił błąd podczas pobierania danych:', error);
    }
});

document.getElementById("logout-button").addEventListener("click", async function() {
    try {
        const response = await fetch('http://localhost:8000/logout', {
            method: 'POST',
            credentials: 'include'  
        });

        if (response.ok) {
            // Udane wylogowanie, przekieruj użytkownika lub zaktualizuj interfejs
            console.log("Wylogowano pomyślnie");
            document.getElementById("logout-button").style.display = "none";
            document.getElementById("login-button").style.display = "block";
            document.getElementById("register-button").style.display = "block";
        } else {
            console.error('Błąd podczas wylogowywania');
        }
    } catch (error) {
        console.error('Wystąpił błąd podczas wylogowywania:', error);
    }
});
