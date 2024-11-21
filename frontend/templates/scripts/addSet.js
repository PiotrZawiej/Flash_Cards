document.getElementById("setForm").addEventListener('submit', async function addSet(event) {
    event.preventDefault();

    const setName = document.getElementById('setName').value;

    try{
        const response = await fetch("http://localhost:8000/create_Set", {
            metchod: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(setName)
        });
        if (response.ok){
            const result = await response.json();
            alert(result.message);
        }else {
            const error =await response.json();
            alert(`Error: ${error.detail}`);
            
        }
    }   catch (error){
        alert('An unexpected error occurred.')
    };
});