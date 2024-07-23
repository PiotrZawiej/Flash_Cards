import sqlite3


def add_content_table(word, description):

    try:
        db = sqlite3.connect('words_data.db') 
        cursor = db.cursor()

        cursor.execute('INSERT INTO words (word, description) values (?, ?)', (word, description))

        db.commit()

    except sqlite3.Error as e:
        print(f"an error occurred:{e}")
    
    finally:
        db.close()



def import_table_content():

    try:
        db = sqlite3.connect('words_data.db')
        cursor = db.cursor()

        cursor.execute('SELECT * FROM words')
        rows = cursor.fetchall()

        return rows

    except sqlite3 as e:
        print(f"an error occurred:{e}")

    finally:
        db.close()
