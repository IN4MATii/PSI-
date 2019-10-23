from decimal import *
# 1
lorem = 'Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. ' \
        'Został po raz pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki. ' \
        'Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym. ' \
        'Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem ' \
        'Ipsum, a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym ' \
        'o realizacji druków na komputerach osobistych, jak Aldus PageMaker'
# 2
imie='Mateusz'
nazwisko='Maślanka'
litera_1=imie[:2]
litera_2=nazwisko[:3]
x=lorem.count(litera_1)
z=lorem.count(litera_2)
print('W tekście jest %i liter "%s" oraz %i liter "%s"' % (x, litera_1, z,litera_2))

# 4
zmienna_typu_string='fajna zmienna typu string'
#print(dir(zmienna_typu_string))
#help(zmienna_typu_string.isalpha())
# def isalpha(self, *args, **kwargs):  # real signature unknown
#       """
#        Return True if the string is an alphabetic string, False otherwise.
#
#        A string is alphabetic if all characters in the string are alphabetic and there
#        is at least one character in the string.
#        """
#        pass

# 5
nazwa=imie + ' ' + nazwisko
print(nazwa[0:16:-1])

# 6
lista=[i for i in range(1,11)]
print(lista)
lista1=[]
for i in range(0, 5, 1):
        lista1.insert(lista[i],i+1)
        res=[i for i in lista if i not in lista1]

print(res)
print(lista1)

# 7
lista2=lista1 + res
lista3=[0]
lista3=lista3+lista2
print(lista3)
lista4=lista3
lista4.sort(reverse=True)
print(lista4)

# 8
student1=('Jacek Zielonka',111111)
student2=('Kamiln Borkowski', 222222)
student3=('Jaroslaw Kaczynski', 333333)
student4=('Janusz Korwin-Mikke', 444444)
krotka_studentow=student1,student2,student3,student4
print(krotka_studentow)

# 10
numery=[111222333,555666000,111222333,444111222,333999888]
print(numery)
numery_zbior=set(numery)
print(numery_zbior)

# 11
for i in range(1,11):
        print(i)

# 12
for i in range(100,20,-5):
        print(i)

