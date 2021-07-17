from math import sqrt

values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 16, 25, 36, 49]
#filtered2 = [n for n in values if sqrt(n) % 2 == 0]           #przy użyciu listcomperhesion
def filtered_values(value):
    filtered = filter(lambda n: sqrt(n) % 2 == 0, value)          #przy urzyciu funkcje + lambda
    return filtered

if __name__ == "__main__":
    print(list(filtered_values(values)))

def test_filtered():
    values = [1, 4, 8, 16]
    score = list(filtered_values(values))
    assert score == [4, 16]




