#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv(r'C:\Users\Admin\Desktop\Anaconda\toy_dataset.csv')
Age = df['Age']
Income = df['Income']
plt.bar(Age,Income)
plt.xlabel('Age')
plt.ylabel('Income')
plt.title('Age vs Income')
plt.show()


# In[ ]:




