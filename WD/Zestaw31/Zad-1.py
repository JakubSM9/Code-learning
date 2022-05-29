import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

labels = ['Hipermarkety', 'Supermarkety', 'Domy Handlowe']
rok2k16 = [6, 33, 1,]
rok2k17 = [8, 28, 3,]

x = np.arange(len(labels))  
width = 0.35  

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, rok2k16, width, label='2016')
rects2 = ax.bar(x + width/2, rok2k17, width, label='2017')

ax.set_title('Informacje o sklepach')
ax.set_xticks(x, labels)
ax.legend()

fig.tight_layout()

plt.show()