import csv
import pandas as pd

def take_question():
    quiz_question = []

    with open('pytania.csv', encoding='utf8') as file_open:
        idx = 1
        for data in file_open:
            result = data.strip().split(';')
            result.insert(0, idx)
            idx += 1
            quiz_question.append(result)
        return quiz_question

quiz_question = take_question()

for indeks in quiz_question:
    if indeks[0] == 2:
        print(indeks)

