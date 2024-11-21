import sqlite3

def import_Words():

    try:
        db = sqlite3.connect('words_data.db')
        cursor = db.cursor()

        cursor.execute('SELECT * FROM Words')
        rows = cursor.fetchall()

        return rows

    except sqlite3 as e:
        print(f"an error occurred:{e}")

    finally:
        db.close()
        
        
def delete_table_content(id):
    try:
        db = sqlite3.connect('words_data.db')
        cursor = db.cursor()
        
        cursor.execute('DELETE FROM Words WHERE id = ?', (id,))
        
        db.commit()
    except sqlite3 as e:
        print(f"an error occurred:{e}")

    finally:
        db.close()


def insert_Words(word, definition):

    try:
        db = sqlite3.connect('words_data.db') 
        cursor = db.cursor()

        cursor.execute('INSERT INTO Words (word, definition) values (?, ?)', (word, definition))

        db.commit()

    except sqlite3.Error as e:
        print(f"an error occurred:{e}")
    
    finally:
        db.close()