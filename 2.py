#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


df = pd.read_csv('/Users/anandabit/Desktop/gapminder-FiveYearData.csv')


# In[3]:


country_df=df['country']


# In[4]:


subset=df[['country', 'continent', 'year']]


# In[5]:


print(subset.head())


# In[6]:


print(df.head())


# In[7]:


print(subset.tail())


# In[8]:


print(df.loc[0])


# In[9]:


print(df.loc[99])


# In[10]:


df.loc[99]


# In[11]:


print(df.tail(n=1))


# In[14]:


print(df.loc[[0,99,999]])


# In[16]:


print(df.iloc[0])


# In[17]:


print(df.iloc[-1])


# In[21]:


print(df.shape)


# In[ ]:




