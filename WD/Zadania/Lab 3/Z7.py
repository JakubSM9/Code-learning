ile = int(input('Ile liczb chcesz podać?'))
list=[]
while ile >0:
    a = int(input('podaj liczbe: '))
    list.append(a)
    ile = ile-1

print(list)

def iloczyn(liczby):
    count = 1
    for x in liczby:
        count = count*x
    print(count)

iloczyn(list)