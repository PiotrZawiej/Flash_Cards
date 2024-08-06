import sqlite3


def add_content_table(word, definition):

    try:
        db = sqlite3.connect('words_data.db') 
        cursor = db.cursor()

        cursor.execute('INSERT INTO words_new (word, definition) values (?, ?)', (word, definition))

        db.commit()

    except sqlite3.Error as e:
        print(f"an error occurred:{e}")
    
    finally:
        db.close()



def import_table_content():

    try:
        db = sqlite3.connect('words_data.db')
        cursor = db.cursor()

        cursor.execute('SELECT * FROM words_new')
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
        
        cursor.execute('DELETE FROM words_new WHERE id = ?', (id,))
        
        db.commit()
    except sqlite3 as e:
        print(f"an error occurred:{e}")

    finally:
        db.close()
        


