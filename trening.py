# operatory arytmetyczne
suma = 1 + 2 * 3 / 4.0
print(suma)

# modulo czyli reszta z dzielenia
reszta = 12 % 5
kwadrat = 5 ** 2
szescian = 5 ** 3

# operacje na napisach
full_name = "Krzysztof" + " " + "Ropiak"
print(full_name)

# ale to ?
spam = "SPAM " * 10
print(spam)

# listy
oceny = [1, 2, 3, 4, 5] * 10
print(oceny)

# operatory porównania
liczba1 = 1
liczba2 = 2
print(liczba1 > liczba2)
print(liczba1 <= liczba2)
print(liczba1 == liczba2)
print(liczba1 != liczba2)

# powyższe porównania zwrócą wartości logiczne czyli True lub False
# na wartościach logicznych możemy również wykonywac operacje
prawda = True
falsz = False
print(prawda and falsz)
print(prawda or falsz)
print(not prawda)
print(not not prawda)
print(bool(prawda or falsz))

całkowita = 5
rzeczywista = 5.6

# przykład rzutowania
rzeczywista = float(56)

# poniżej kolejny przykład
liczba_str = "123"
liczba = int(liczba_str)
print(type(liczba))

# zmienne można również zadeklarować w jednej linii
a, b = 3, 4

# cwiczenie na stringach
imie="PATRYKENSSSOO"
nazwisko='Brudzynski'

print(nazwisko[3])
print(nazwisko[0])
print(nazwisko[-2]) #liczy od tyłu
print(imie[0] + imie[-2] + imie[2:6]) #wypisuje miedzy indexem miedzy 2 a 6
print(imie + nazwisko[6:])  #nie trzeba podawac ostatniego index
print(imie.count('o')) #zlicza ilosc danej literki w ciagu
print('Jestes szalona'.count('e')) #zlicza literki juz w trakcie definiowania ciagu
print(imie.lower())
print(imie)
print(len(imie))
wyznanie='lubie %s' % 'pythona'
print(wyznanie)
wonsz = "Python"
print("Lubię %sa" % wonsz)
print("Lubię %s oraz %sa" % ("Pythona", wonsz))

# %s oznacza, że w miejsce tego znacznika będzie podstawiany ciąg tekstowy
# %i - to liczba całkowita
# %f - liczba rzeczywista lub inaczej zmiennoprzecinkowa
# %x lub #X - liczba całkowita zapisana w formie szesnastkowej
print("Używamy wersji Python %i" % 3)
print("A dokładniej Python %f" % 3.5)
print("Chociaż lepiej to zapisać jako Python %.1f" % 3.5)
print("A kolejną glówną wersją Pythona może być wersja %.4f" % 3.6666)
print("A może będzie to wersja %.1f ?" % 3.6666)
print("A może jednak %.f ?" % 3.6666)
wersja = 4
print("A %i w systemie szesnastkowym to %X" % (wersja, wersja))
print("A %i * %i szesnastkowo daje %X" % (wersja, wersja, wersja*wersja))
