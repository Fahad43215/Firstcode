import sys
import matplotlib


import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('KINDEX.csv')
df.plot()
plt.show()
plt.xlabel('Time')
plt.ylabel('K')
plt.title('K values over Time')
plt.legend



