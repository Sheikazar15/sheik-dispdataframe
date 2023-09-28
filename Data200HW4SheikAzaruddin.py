#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv(r'C:\Users\Admin\Desktop\Anaconda\toy_dataset.csv')

# Create a subplot with 1 row and 2 columns
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Plot the bar chart on the first subplot
axes[0].bar(df['Age'], df['Income'])
axes[0].set_xlabel('Age')
axes[0].set_ylabel('Income')
axes[0].set_title('Age vs Income (Bar Chart)')

# Plot the pie chart on the second subplot
illness_counts = df['Illness'].value_counts()
axes[1].pie(illness_counts, labels=illness_counts.index, autopct='%1.1f%%')
axes[1].set_title('Illness Distribution (Pie Chart)')

# Adjust spacing between subplots
plt.tight_layout()

# Show both charts
plt.show()

# Display in Streamlit
st.pyplot(x)


# In[ ]:




