from random import randint

for a in range(10):
    aaa = randint(1,10)
    print(aaa)
quiz_question = []
with open('pytania.csv', encoding='utf8') as file_open:
    for data in file_open:
        result = data.strip().split(';')
        quiz_question.append(result)

    list_number = list(range(1, len(quiz_question)+1))

    new_list = dict(zip(list_number, quiz_question))
    print(new_list)

