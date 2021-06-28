

def remove_volwels(text: str) -> str:
    volwels = 'aeyoiąęAEYOI'
    # result = ''
    #
    # for char in text:
    #     if char not in volwels:
    #         result += char
    #
    # return result
    return ''.join(char for char in str(text) if char not in volwels)


def test_remove_volwels():
    assert remove_volwels('Ala ma kota') == 'l m kt'
    assert remove_volwels('Wolę Pythona') == 'Wl Pthn'
    assert remove_volwels('') == ''

def test_remove_volwels_a():
    assert remove_volwels(10234) == '10234'

if __name__ == '__main__':
    print(remove_volwels('krasnoludek'))

