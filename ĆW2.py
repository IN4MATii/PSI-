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