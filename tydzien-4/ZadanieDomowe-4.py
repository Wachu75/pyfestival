def group_them(**kwargs):
    for key, value in kwargs.items():
        print(f'{key.capitalize()} is {value}')


def test_group_them(capsys):
    #given
    group_them(wall='red', tomato='red', light='yellow')
    out, err = capsys.readouterr()
    #them
    assert out == 'Wall is red\nTomato is red\nLight is yellow\n'

group_them(wall='red', tomato='red', light='yellow')