import numpy as np
#Zad1
#Utwórz dwie macierze 1x3 różnych wartości a następnie wykonaj operację mnożenia

# a = np.array([3, 4, 5])
# b = np.array([6, 2, 4])
# c = a * b
# print(c)

#Zad2
#Utwórz macierz 3x3 oraz 4x4 i znajdź najniższe wartości dla każdej kolumny i każdego rzędu

# a = np.array([[3, 7, 5], [6, 1, 9], [2, 7, 8]])
# b = np.array([[5, 1, 6, 8], [3, 6, 2, 7], [9, 3, 7, 5], [4, 4, 2, 1]])
# print(a)
# print(b)
#
# print(a.min(axis=0))
# print(a.min(axis=1))
# print(b.min(axis=0))
# print(a.min(axis=1))

#Zad3
#Wykorzystaj macierze z zadania pierwszego i wykonaj iloczyn macierzy

# a = np.array([3, 4, 5])
# b = np.array([6, 2, 4])
# c = np.dot(a, b)
# print(c)

#Zad4
#Utwórz dwie macierze 1x3 gdzie pierwsza z nich będzie zawierała liczby całkowite, a druga
#liczby rzeczywiste. Następnie wykonaj na nich operację mnożenia.

# a = np.array([3, 4, 5])
# b = np.linspace(3, 10, 3)
# c = a * b
# print(c)

#Zad5,6,7

#Utwórz macierz 2x3 różnych wartości a następnie wylicz sinus dla każdej z jej wartości i
#zapisz do zmiennej “a”.

# c = np.array([[60, 31], [45, 78], [15, 50]])
# a = np.sin(c)
# print(a)
#
#
# d = np.array([[47, 24], [64, 28], [19, 33]])
# b = np.cos(d)
# print(b)
# print("")
# dodawanie = np.add(a,b)
# print(dodawanie)

#Zad8
#Wygeneruj macierz 3x3 i wyświetl w pętli każdy z rzędów

# a = np.array([[3, 7, 5], [6, 1, 9], [2, 7, 8]])
# for b in a:
#     print(b)
#     print("")

#Zad9
#Wygeneruj macierz 3x3 i wyświetl w pętli każdy element korzystając z opcji “spłaszczenia”
#macierzy. (użyj funkcji flat()

# a = np.array([[3, 7, 5], [6, 1, 9], [2, 7, 8]])
# for b in a.flat:
#     print(b)
#     print("")

#Zad10
#Wygeneruj macierz 9x9 a następnie zmień jej kształt. Jakie mamy możliwości i dlaczego

# macierz = np.arange(0,81,1).reshape(9,9)
# print(macierz)
#
# macierz_1 = macierz.reshape(3,27)
# print(macierz_1)
# macierz_2 = macierz.reshape(27,3)
# print(macierz_2)
# macierz_3 = macierz.reshape(81,1)
# print(macierz_3)
# macierz_4 = macierz.ravel()
# print(macierz_4)

#Zad11
#Wygeneruj macierz płaską (wektor) i przekształć ją na macierz 3x4. Wygeneruj w ten sposób
#jeszcze kombinacje 4x3 i 2x6. Spłaszcz każdą z nich i wyświetl wyniki. Czy są identyczne

'''a = np.array([3, 7, 5, 6, 1, 9, 2, 7, 8, 6, 3, 6])
print(a)
macierz_1 = a.reshape(3, 4)
print(macierz_1)
print(macierz_1.ravel())
macierz_2 = macierz_1.reshape(4,3)
print(macierz_2)
print(macierz_2.ravel())
macierz_3 = macierz_1.reshape(2,6)
print(macierz_3)
print(macierz_3.ravel())
'''