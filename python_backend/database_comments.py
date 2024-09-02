import sqlite3


def add_content_table(word, definition):

    try:
        db = sqlite3.connect('words_data.db') 
        cursor = db.cursor()

        cursor.execute('INSERT INTO Words (word, definition) values (?, ?)', (word, definition))

        db.commit()

    except sqlite3.Error as e:
        print(f"an error occurred:{e}")
    
    finally:
        db.close()



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
        

def Insert_User(email, username, password, birth_date):
    try:
        db = sqlite3.connect("words_data.db")
        cursor = db.cursor()
        
        cursor.execute('INSERT INTO Users (email, username, password, birth_date) VALUES (?, ?, ?, ?)', (email, username, password, birth_date))
        
        db.commit()
        
    except sqlite3.Error as e:
        print(f"an error occurred:{e}")
    finally:
        db.close()
        
def import_User_password(idetifier: str):
    try:
        db = sqlite3.connect('words_data.db')
        cursor = db.cursor()

        cursor.execute('SELECT password FROM Users WHERE username = ? OR email = ?', (idetifier,idetifier))
        row = cursor.fetchone()  

        if row:
            return row[0]  
        else:
            return None

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return None

    finally:
        db.close()
        
def import_User_id(idetifier: str):
    try:
        db = sqlite3.connect('words_data.db')
        cursor = db.cursor()

        cursor.execute('SELECT user_id FROM Users WHERE username = ? OR email = ?', (idetifier,idetifier))
        row = cursor.fetchone()  

        if row:
            return row[0]  
        else:
            return None

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return None

    finally:
        db.close()

        

        
# def create_tables():
#     try:
#         db = sqlite3.connect('words_data.db')
#         cursor = db.cursor()
        
#         cursor.execute('''
#         CREATE TABLE IF NOT EXISTS Users (
#             user_id INTEGER PRIMARY KEY AUTOINCREMENT,
#             email VARCHAR(255) NOT NULL UNIQUE,
#             username VARCHAR(100) NOT NULL,
#             password VARCHAR(255) NOT NULL,
#             birth_date DATE NOT NULL
#         );
#         ''')
        
#         db.commit()
#     except sqlite3.Error as e:
#         print(f"An error occurred: {e}")
#     finally:
#         db.close()



        
        
