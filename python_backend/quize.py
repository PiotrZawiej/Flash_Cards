import python_backend.database_comments as dbc
import random as r

def quiz():

    quiz_words = dbc.import_table_content()

    while quiz_words:

        for row in quiz_words:
            print("what's that word: \n")
            answer = input(row[1])

            if row[0] == answer:
                print("word correct!!! \n")
                del quiz_words[quiz_words.index(row)]

            else:
                print("wrong answer \n")
                r.shuffle(quiz_words)
    
    print("Quiz completed!!!")
