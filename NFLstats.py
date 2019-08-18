#!/usr/bin/env python
# coding: utf-8

# In[12]:


import pandas as pd


# In[13]:


import numpy as np


# In[14]:


import matplotlib.pyplot as plt


# In[15]:


QB = pd.read_csv('2018QBstats.csv')


# In[16]:


QB.head(5)


# In[17]:


TE = pd.read_csv('2019TEstats.csv')


# In[18]:


TE.head(3)


# In[19]:


WR = pd.read_csv('2018Receiversstats.csv')


# In[20]:


WR.head(3)


# In[25]:


RB = pd.read_csv('2018RB.csv')


# In[26]:


RB.head(3)


# In[27]:


DEF = pd.read_csv('2018def.csv')


# In[28]:


DEF.head(3)


# In[37]:


def tot_rank(i): 
    T = (DEF['RK'][i]+DEF['RK.1'][i]+DEF['RK.2'][i]+DEF['RK.3'][i]+DEF['RK.4'][i]+DEF['RK.5'][i])/6 
    return(T)


# In[38]:


tot_rank(0)


# In[39]:


Y = list(range(0,32))


# In[41]:


Drank = tot_rank(Y)


# In[36]:


72/6


# In[42]:


QB.head(5)


# In[43]:


def Ratio(i): 
    R = QB['TD'][i]/QB['INT'][i]
    return(R)


# In[45]:


Z = list(range(0,33))


# In[47]:


TD_INT = Ratio(Z)


# In[48]:


plt.plot(TD_INT)


# In[49]:


TD_INT


# In[ ]:




