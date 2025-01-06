import sqlite3


def new_Flashcardset(name, user_id):
    try:
        with sqlite3.connect("words_data.db") as db:
            cursor = db.cursor()
            cursor.execute('INSERT INTO FlashcardSets (set_name, user_id) values (?, ?)', (name, user_id, ))
            db.commit()
    except sqlite3.Error as e:
        print(f"an error occurred:{e}")



def select_Flashcard_SetID():
    try:
        with sqlite3.connect("words_data.db") as db:
            cursor = db.cursor()
            cursor.execute('Select * from FlashcardSets')
            results = cursor.fetchall()
        return results
    except sqlite3.Error as e:
        print(f"an error occurred:{e}")



def delete_Flashcard_set(set_id):
    try:
        with sqlite3.connect("words_data.db") as db:
            cursor = db.cursor()
            cursor.execute('DELETE FROM FlashcardSets WHERE set_id = ?', (set_id,))
            db.commit()
    except sqlite3.Error as e:
        print(f"an error occurred:{e}")
    

