import sqlite3


def new_Flashcardset(name : str):

    try:
        db = sqlite3.connect("words_data.db")
        cursor = db.cursor()

        cursor.execute('INSERT INTO FlashcardSets (set_name) values (?)', (name,))

        db.commit()
    
    except sqlite3.Error as e:
        print(f"an error occurred:{e}")

    finally:
        db.close()


def select_Flashcard_SetID():

    try:
        db = sqlite3.connect("words_data.db")
        cursor = db.cursor()

        cursor.execute('Select set_id from FlashcardSets')

    
    except sqlite3.Error as e:
        print(f"an error occurred:{e}")

    finally:
        db.close()


def delete_Flashcard_set(set_id):

    try:
        db = sqlite3.connect("words_data.db")
        cursor = db.cursor()

        cursor.execute('DELETE FROM FlashcardSets WHERE set_id = ?', (set_id,))

        db.commit()

    except sqlite3.Error as e:
        print(f"an error occurred:{e}")
    
    finally:
        db.close()