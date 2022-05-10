#zadanie2
import random
randomlist=[]
for i in range (10):
    n=random.randint(1,100)
    randomlist.append(n)
    print(randomlist)
nowalista= [x for x in randomlist if x%2==0]
print(nowalista)