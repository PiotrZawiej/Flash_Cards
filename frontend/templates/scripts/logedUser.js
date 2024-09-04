document.addEventListener("DOMContentLoaded", async function() {
    try {
        // Wysłanie zapytania do serwera, aby sprawdzić, czy użytkownik jest zalogowany
        const response = await fetch('http://localhost:8000/main-page', {
            method: 'GET',
            credentials: 'include'  // Uwzględnij ciasteczka w zapytaniu
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

// Funkcja do obsługi wylogowania
document.getElementById("logout-button").addEventListener("click", async function() {
    await fetch('http://localhost:8000/logout', {
        method: 'POST',
        credentials: 'include'
    });

    document.cookie = "user_id=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
    window.location.href = "login.html";
});
