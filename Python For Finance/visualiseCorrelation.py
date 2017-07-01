import pandas as pd
import numpy as np
import seaborn as sea
import matplotlib.pyplot as plt

df = pd.read_csv('sp500_joined_closes.csv')
df = df.set_index("Date")

corr = df.corr()

print("hi ")
sea.heatmap(corr)

