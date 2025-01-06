document.getElementById("setForm").addEventListener('submit', async function addSet(event) {
    event.preventDefault();

    const setName = document.getElementById('setName').value;
    const userID = document.cookie
    console.log(document.cookie)

    try {
        const response = await fetch("http://127.0.0.1:8000/sets/create_Set", {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ set_name: setName, user_id: userID })
        });

        if (response.ok) {
            const result = await response.json();
            alert(result.message);
        } else {
            const error = await response.json();
            alert(`Error: ${error.detail}`);
        }
    } catch (error) {
        alert('An unexpected error occurred.');
    }
});
