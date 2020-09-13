# soal no 1

from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/vaksakalli/datasets/master/diamonds.csv')

fig, ax = plt.subplots(figsize=(13, 13))
palette="ch:r=-.2,d=.3_r"

sns.scatterplot(data = df, x = 'carat', y = 'price', hue = 'clarity', palette = palette, size = "depth", sizes = (5, 7), linewidth = 0.05)

# soal no 2

def hexbin(x, y, color, **kwargs):
    cmap = sns.light_palette(color, as_cmap=True)
    plt.hexbin(x, y, gridsize=15, cmap=cmap, **kwargs)
    
with sns.axes_style("dark"):
    g = sns.FacetGrid(df, hue="cut", col="cut", height=4)
g.map(hexbin, "carat", "price", extent=[0, 3.0, 0, 20000])

# soal no 3

df = df.sample(n=300, random_state=123)
df_new=df[['carat','depth','table','price','cut']]
sns.pairplot(df_new, hue='cut',corner=True,markers=['+','o','s','D','x'])
plt.show()

# soal no 4

with sns.axes_style('white'):
    sns.jointplot(df['carat'], df['price'], kind='kde')
    
sns.jointplot("carat", "price", data = df, kind = 'reg', xlim = (0, 2.5), ylim = (0, 20000))