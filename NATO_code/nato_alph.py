import pandas

data = pandas.read_csv("C:/Users/mirun/Documents/Learning/Python-exercices/NATO_code/code.csv")
form_data = {row.letter: row.code for (index, row) in data.iterrows()}

def word_function():
    word = input("Write your word: ")
    letters_word = [item.upper() for item in word]
    try:
        coded_word = [form_data[item] for item in letters_word]
    except KeyError:
        print("Thw word must contain only letters!")
        word_function()
    else:
        print(coded_word)

word_function()
