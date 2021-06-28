# co testujemy ?
#   logikę naszej aplikacji
#   napisany przez nas kod
#   kod który modyfikujemy aby upewnić się że nic nie zepsuliśmy
# piramida testów

#  instalujemy
# pip install pytest

# uruchamiamy testy
# python -m pytest nazwa_programu_do_testowania.py

# test jest to zwykła funkcja zaczynająca się od słowa test

def test_cos():
    pass


# zawierają kod napisany w pythonie
# dobry test składa się z:  - Given   -When   - Then
# testy muszą! działać na tym samym zestawie danych nie może być zależny od innej części kodu!
# nie generujemy danych np losowych muszą to być stałe dane

def add_numbers(a: int, b: int) -> int:
    return a + b


def test_add_numbers():
    a = 2  # Given
    b = 3  # Given
    value = add_numbers(a, b)  # When
    assert value == 5  # Then sprawdzamy czy na podstawie konkretnych danych wynik jest prawidłowy
    # sprawdzajmy skrajne przypadki


def rectangle_area(a: int, b: int) -> int:
    if a < 0 or b < 0:
        return 0
    return a * b


def test_rectangle_area():
    assert rectangle_area(2, 10) == 20
    assert rectangle_area(0, 10) == 0
    assert rectangle_area(-2, 10) == 0
# jeżeli coś pójdzie nie tak to powstaje folder .pytest_casch
# ponowne uruchomienie testowania zaczyna się od miejsca gdzie pierwszy test nie przeszedł
