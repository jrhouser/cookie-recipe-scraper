import pandas as pd
import numpy as np
import pylab as plt

plt.style.use('ggplot')


ratings = pd.read_csv('recipe_stars.csv')

plt.figure(figsize=(10,5))
plt.hist(ratings['stars'])
plt.xlabel('stars')
plt.ylabel('Number of stars')
plt.title('Distribution of stars for all cookies')
plt.savefig('./figure2.png')
plt.show()

