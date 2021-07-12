# Przygotuj funkcję, która odbierze dwa punkty w postaci tupli (x, y). Wynikiem
# powinna być długość odcinka utworzonego w wyniku połączenia tych dwóch
# punktów.
# |AB| = sqrt(pow(x2 - x1) + pow(y2-y1))
from math import sqrt, pow

def odcinek(x1,x2,y1,y2):
    return sqrt(pow((x2-x1),2)+pow((y2-y1),2))

print('podaj współżędne wierzchołka A a następnie B w postaci liczby całkowitej -> x1 "Enter" y1 "Enter" itd. \n' )
x1 = int(input('współżędne x1:'))
y1 = int(input('współżędne y1:'))
x2 = int(input('współżędne x2:'))
y2 = int(input('współżędne y2:'))

print('długość odcinka x,y =',odcinek(x1,x2,y1,y2))

