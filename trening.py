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
# Chociaż możliwości przy korzystaniu z mechanizmów powyżej są spore,
# to i kilka wad się również znajdzie. Trzeba pilnować zarówno liczby argumentów jak
# i ich kolejności. Konieczne jest powielanie tej samej zmiennej jeżeli kilka
# razy jest wykorzystywana w formatowanym ciągu. Spójrzmy na inne możliwości.
print("Lubię %(jezyk)s" % {"jezyk": "Pythona"})
print("Lubię %(jezyk)s a czy Ty lubisz %(jezyk)s ?" % {"jezyk": "Pythona"})

# wadą jest dość duża ilość dodatkowego kodu do napisania, ale nazwy zmiennych
# w ciągu pozwalają na ich szybką identyfikację i wielokrotne wykorzystanie w
# dowolnej kolejności
# poniżej kolejny sposób
print("Lubię język {1} oraz {0}".format("Java", "Python"))

# w nowej wersji języka Python możliwe jest również odwoływanie się do elementów kolekcji
# lub pól klasy
class Osoba:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko
kr = Osoba("Krzysztof", "Ropiak")
print("Tą osobą jest {0.imie} {0.nazwisko}".format(kr))

## Lub mój ulubiony sposób (Łukasz) w następujący sposób:
print(f'Tą osobą jest {kr.imie} {kr.nazwisko}')

lorem = 'Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. ' \
        'Został po raz pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki. ' \
        'Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym. ' \
        'Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem ' \
        'Ipsum, a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym ' \
        'o realizacji druków na komputerach osobistych, jak Aldus PageMaker'
imie='Mateusz'
nazwisko='Maślanka'
litera_1=imie[:2]
litera_2=nazwisko[:3]
x=lorem.count(litera_1)
z=lorem.count(litera_2)
print(x)
print(z)
print('W tekście jest %i liter %s oraz %i liter %s' % (x, litera_1, z,litera_2))
lista=[]
lista2=list(10)
lista3=[1,2,3]
lista4 = ["a", 5, "Python", 7.8]
print(lista3)
lista5=[lista3,lista4]
print(lista5)
lista3.extend(lista4)
print(lista3)

lista7 = [7, 9, 3, 1]
posortowana = lista7.sort()
print(lista7)
print(posortowana)

skala=[1,2,3,4,5]
skala.append(6)
print(skala)
skala[6:]=[7]
print(skala)
skala.insert(6,7)
print(skala)
skala.pop()
print(skala)
skala.pop(2)
print(skala)
lista6=[1,2,3,4,5,6,7,8,9,10]
print(lista2)
print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
# tworzymy krotke
krotka = (1, 2, "Jacek", "ma")
krotka_liczb = krotka[:2]
print(krotka_liczb)
krotka_stringow = krotka[2:]
print(krotka_stringow)
nowa_krotka = tuple()
najnowsza_krotka = tuple([1, 2, 3])