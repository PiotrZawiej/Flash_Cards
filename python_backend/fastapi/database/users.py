import sqlite3


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


def import_UserName_by_id(id: str) -> str:
    try:
        with sqlite3.connect('words_data.db') as db:
            cursor = db.cursor()
            cursor.execute('SELECT username FROM Users WHERE user_id = ?', (id,))
            row = cursor.fetchone()

            if row:
                return row[0]
            return None

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return None