def count_letters(text, start='(', end=')'):
    should_count = False
    counter = 0
    temp_counter = 0
    for char in text:
        if char == end:
            should_count = False
            counter += temp_counter
            temp_counter = 0

        if should_count:
            counter += 1

        if char == start:
            should_count = True

    return counter

def test_count_leters_without_end_bracket():
    assert count_letters('test(without end bracket') == 19

def test_cont_letters_once():
    assert count_letters('ala ma (kota)') == 4


def test_count_letters_none():
    assert count_letters('samuraj') == 0
    assert count_letters('py(th)on', '<', '>') == 0


def test_count_letters_brackets():
    assert count_letters('<nauka> <programowania>', '<', '>') == 18
    assert count_letters('(nauka) (programowania)') == 18
