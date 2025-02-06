import sys
import matplotlib


import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('weather.csv')


df.plot()

plt.show()
