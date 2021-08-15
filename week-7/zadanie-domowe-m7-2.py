import csv
from _csv import reader
from random import choice

import pandas as pd

class Question:
    def __init__(self, question: str, answers: list, correct_answer: int):
        self.answers = answers
        self.question = question
        self.correct_answer = correct_answer

    def display(self):
        response = f'Pytanie: {self.question}\n'
        for no, answer in enumerate(self.answers, start=1):
            response += f'{no}. {answer} \n'
        return response

    def check_answer(self, answer_id):
        return self.correct_answer == answer_id


    # def ReadQuestionFromFile(self, question_file):
    #     with open(question_file, encoding='utf8') as data:
    #         iterator_data = csv.reader(data, delimeter=';')

class Quiz:
    def __init__(self, question_file):
        self.questions = []
        self.readQuestionFromFile(question_file)

    def readQuestionFromFile(self, question_file):
        with open(question_file, encoding='utf8') as data:
            iterator_data = reader(data, delimiter=';')
            for row in iterator_data:
                question = row.pop(0)
                correct_answer = row.pop(0)
                answers = row
                if len(answers) != 3:
                    raise ValueError('niemoge załadować pytań')
                self.questions.append(Question(question, answers, correct_answer))

    def run(self):
        ask_question = True
        result = 0
        while ask_question:
            try:

                question = choice(self.questions)
                print(question.display())
                self.questions.remove(question)
                answer = input('prosze podac poprawną odpowiedź: ')
                if question.check_answer(answer):
                    result += 1
                else:
                    break
            except IndexError:
                print(f'wygrywasz {result}')
               # ask_question = False
        print(f'wynik to {result}')


if __name__ == '__main__':
    try:
        quiz = Quiz('pytania.csv')
        quiz.run()
    except FileNotFoundError:
        print("plik nie istnieje")
    except ValueError:
        print("coś nie tak z pytaniami")
    except KeyboardInterrupt:
        print('koniec')


