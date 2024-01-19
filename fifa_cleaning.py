#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv(r'C:\Users\Admin\Desktop\csv files\fifa21 raw data v2.csv')
df


# In[3]:


df.head()


# In[12]:


df.columns


# In[14]:


df.dtypes


# In[5]:


df['Club'].dtypes


# In[6]:


df['Club'].unique()


# In[7]:


df['Club'] = df['Club'].str.strip()


# In[9]:


df['Club'].unique()


# In[15]:


df['Contract'].unique()


# In[16]:


df['Contract'].dtypes


# In[18]:


for index, row in df.iterrows():
    if 'On Loan' in row['Contract'] or 'Free' in row['Contract']:
        print(row['Contract'])


# In[ ]:





# In[ ]:




