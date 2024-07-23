import python_backend.database_comments as dbc
import python_backend.quize as q


def menu():
    choice = input("Please choose what you're going to do\n"+
                   "1. Update words and defnitions \n" + 
                   "2. Learn words \n" +
                   "3. Quiz \n" +
                   "4. Quit \n")

    match choice:

        case "1":
            print("please tipe word")
            word = input()
            print("pls tipe definition of word")
            description = input()

            dbc.add_content_table(word, description)

        case "2":
            for r in dbc.import_table_content():
                print(r[0] + " - " + r[1])
        
        case "3":
            q.quiz()

        case "4":
            print("Closing program")

        case _:
            print("Wrong statement")