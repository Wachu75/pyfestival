leters = ('"A";"Ą";"B";"C";"Ć";"D";"E";"Ę";"F";"G";"H";"I";"J";"K";"L";"Ł";"M";"N";"Ń";"O";"Ó";"P";"Q";"R";"S";"Ś";"T";"U";"V";"W";"X";"Y";"Z";"Ż";"Ź"' )
leters = leters.replace(';', '').replace('"', '')

print(leters)

alfabet = ('"A","Ą","B","C","Ć","D","E","Ę","F","G","H","I","J","K","L","Ł","M","N","Ń","O","Ó","P","Q","R","S","Ś","T","U","V","W","X","Y","Z","Ż","Ź"')
alfabet1 = "A,Ą,B,C,Ć,D,E,Ę,F,G,H,I,J,K,L,Ł,M,N,Ń,O,Ó,P,Q,R,S,Ś,T,U,V,W,X,Y,Z,Ż,Ź"
alfabet2 = "AĄBCĆDEĘFGHIJKLŁMNŃOÓPQRSŚTUVWXYZŻŹ"
#for a in alfabet:
#    print(a)
    #leter = (chr(a))
    #pod[chr(a)] = a
#leters = ("".join("{!r},".format(v) for v in leters))
# print(pod)
#print("{" + "\n\t" + "\n\t".join("{!s} :\t{!r} ,".format(v, k) for k, v in pod.items()) + "\n" + "}")

for a in range(5):
    print(alfabet2[a])

alfabet = "AĄBCĆDEĘFGHIJKLŁMNŃOÓPQRSŚTUVWXYZŻŹ"
lehgth = len(alfabet)
print(lehgth)
for i in range(len(alfabet)):
    print("litera : ", alfabet[i])

h = "hasło do odgadnięcia"
h.upper()
print(h.upper())
pasword = "HASŁO DO ODGADNIĘCIA"
hiden_pasword = ""
def hide_pasword_for_guesses(pasword):
    # zamiana hasła na znaki '-'
    global hiden_pasword
    for i in range(len(pasword)):
      if pasword[i] != ' ':
          hiden_pasword +="-"

      else:
          hiden_pasword +=" "
    #print(hiden_pasword)
    return hiden_pasword

pasword1 = hide_pasword_for_guesses(pasword)
pasword1 = list(pasword1)
print(pasword1)
lista = ['-', '-', '-', '-', '-', ' ', '-', '-', ' ', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-']
lista1 = list(lista)
print(lista1)