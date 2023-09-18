#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
df = pd.read_csv(r'C:C:\Users\Admin\Desktop\Data Analytics Sem-1\DATA 200\toy_dataset.csv')
Age = df['Age']
Income = df['Income']
plt.bar(Age,Income)
plt.xlabel('Age')
plt.ylabel('Income')
plt.title('Age vs Income')
plt.show()
x = plt.show()
st.pyplot(x)


# In[ ]:




