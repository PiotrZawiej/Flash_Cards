
export function createDeleteButton(WordItem, wordObj){
    const deleteButton = document.createElement('button');
    deleteButton.textContent = "Delete";
    deleteButton.className = "delete-button"


    deleteButton.addEventListener('click',async function handleDelete(){
        event.stopPropagation

        try{
            const response = await fetch('http://localhost:8000/learn_words/${wordObj.id}', {
                method: 'DELETE'
            });
            
            
            if(response.ok){
                WordItem.remove
            }else{
                console.error('Error deleting word:', response.statusText);
            }
        }catch (error){
            console.error('Error deleting word:', error);
        }
        
    })

    return deleteButton;
}
    