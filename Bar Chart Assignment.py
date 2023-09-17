#!/usr/bin/env python
# coding: utf-8

# In[2]:


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


# In[4]:


import pandas as pd
df = pd.read_csv(r'C:\Users\Admin\Desktop\Anaconda\toy_dataset.csv')
Age = df['Number']
Income = df['Income']
plt.plot(Age,Income)
plt.xlabel('Number')
plt.ylabel('Income')
plt.title('Number vs Income')
plt.show()


# In[5]:


import pandas as pd
df = pd.read_csv(r'C:\Users\Admin\Desktop\Anaconda\toy_dataset.csv')
Age = df['Number']
Income = df['Income']
plt.scatter(Age,Income)
plt.xlabel('Number')
plt.ylabel('Income')
plt.title('Number vs Income')
plt.show()


# In[13]:


import pandas as pd
df = pd.read_csv(r'C:\Users\Admin\Desktop\Anaconda\toy_dataset.csv')
Age = df['Number']
Income = df['Income']
plt.pie(Age,Income)
plt.xlabel('Number')
plt.ylabel('Income')
plt.title('Number vs Income')
plt.show()


# In[9]:


import pandas as pd
df = pd.read_csv(r'C:\Users\Admin\Desktop\Anaconda\toy_dataset.csv')
plt.boxplot(df)
plt.xlabel('Number')
plt.ylabel('Income')
plt.title('Number vs Income')
plt.show()


# In[8]:


plt.boxplot(df)
plt.xlabel('X-axis Label')
plt.ylabel('Value')
plt.title('Box Plot Example')
plt.show()


# In[12]:


import matplotlib.pyplot as plt

data = pd.read_csv(r'C:\Users\Admin\Desktop\Anaconda\toy_dataset.csv')

plt.pie(data)
plt.xlabel('X-axis Label')
plt.ylabel('Value')
plt.title('Box Plot Example')
plt.show()


# In[15]:


import pandas as pd
df = pd.read_csv(r'C:\Users\Admin\Desktop\Anaconda\toy_dataset.csv')
Age = df['Number']
Income = df['Income']
plt.pie(Age,Income,autopct='%1.1f%%', startangle=140)
plt.xlabel('Number')
plt.ylabel('Income')
plt.title('Number vs Income')
plt.show()


# In[17]:


import pandas as pd
df = pd.read_csv(r'C:\Users\Admin\Desktop\Anaconda\toy_dataset.csv')

Income = df['Income']
plt.pie(Income,autopct='%1.1f%%', startangle=140)

plt.title('Number vs Income')
plt.show()


# In[18]:


import matplotlib.pyplot as plt

data = pd.read_csv(r'C:\Users\Admin\Desktop\Anaconda\toy_dataset.csv')

plt.boxplot(data)
plt.xlabel('X-axis Label')
plt.ylabel('Value')
plt.title('Box Plot Example')
plt.show()


# In[20]:


import pandas as pd
df = pd.read_csv(r'C:\Users\Admin\Desktop\Anaconda\Fish.csv')
Weight = df['Weight']
Height = df['Height']
plt.plot(Weight,Height)
plt.xlabel('Weight')
plt.ylabel('Height')
plt.title('Weight vs Height')
plt.show()


# In[21]:


import pandas as pd
df = pd.read_csv(r'C:\Users\Admin\Desktop\Anaconda\Real_estate.csv')
no = df['number_of_convenience_stores']
area = df['house_price_of_unit_area']
plt.plot(no,area)
plt.xlabel('Number')
plt.ylabel('Area')
plt.title('Number vs Area')
plt.show()


# In[23]:


import pandas as pd
df = pd.read_csv(r'C:\Users\Admin\Desktop\Anaconda\Real_estate.csv')
no = df['latitude']
area = df['longitude']
plt.plot(no,area)
plt.xlabel('Number')
plt.ylabel('Area')
plt.title('Number vs Area')
plt.show()


# In[ ]:




