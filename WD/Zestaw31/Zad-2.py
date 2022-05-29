import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_excel(r'WD\Zestaw31\motocykle31.xlsx')
print(df)

lata = list(df.groupby('Rok').size())
print(lata)
wartosc = list(df.groupby('Wartość').size())
print(wartosc)

plt.plot(lata,wartosc,'r-')
plt.ylabel('')
plt.xlabel('')
plt.title('')

plt.show()