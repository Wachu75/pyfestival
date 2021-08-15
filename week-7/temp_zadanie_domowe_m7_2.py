import copy
import csv
from typing import List
from random import randint
import pandas as pd

def take_question():

    with open('pytania.csv', encoding='utf8') as file_open:
        iterator = csv.reader(file_open, delimiter=';')
        #iterator1 = csv.reader(file_open, delimiter=';')
        #print(list(iterator1)) # rzutowanie na list nawet gdy mam iterator1 = csv.re  nic nie daje zmieniam otwarty plik i dupa blada!!!
        for question in iterator:
            print(question)
            print(question.pop(0)) # .pop(id) zdejmuje !!! z listy element na indexie id przy czym tworzona jest tym samym nowa lista
            print(question)
            print(question.pop(0)) # która na indexie 0 ma już tą wartość co wcześniej była na indeksie 1 !!! lista jest krótsza!
            print(question)



quiz_question = take_question()


