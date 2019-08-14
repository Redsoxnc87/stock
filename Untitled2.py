#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import numpy as np


# In[3]:


import matplotlib.pyplot as plt


# In[4]:


VIX = pd.read_csv('Alpavdaily_VIX.csv')


# In[5]:


VIX.head(3)


# In[6]:


GLD = pd.read_csv('alphavantagedaily_GLD.csv')


# In[7]:


GLD.head(3)


# In[9]:


SPY = pd.read_csv('Alphavdaily_SPY.csv')


# In[10]:


SPY.head(3)


# In[11]:


USD = pd.read_csv('Alphavantageusdolindexdaily_DXY.csv')


# In[13]:


USD.head(8)


# In[14]:


def AVG_GLD(i): 
    G = (GLD['open'][i]+GLD['high'][i]+GLD['low'][i]+GLD['close'][i])/4
    return(G)


# In[17]:


M = list(range(0,99))


# In[28]:


Gold = AVG_GLD(M)


# In[29]:


def AVG_SPY(i): 
    S = (SPY['open'][i]+SPY['high'][i]+SPY['low'][i]+SPY['close'][i])/4
    return(S)


# In[30]:


SandP =AVG_SPY(M)


# In[31]:


def AVG_VIX(i): 
    V = (VIX['open'][i]+VIX['high'][i]+VIX['low'][i]+VIX['close'][i])/4
    return(V)


# In[32]:


Vol= AVG_VIX(M)


# In[33]:


plt.style.use('seaborn')


# In[37]:


plt.plot(M, Gold, Vol)


# In[42]:


plt.plot(M, Gold)


# In[43]:


H = GLD['high']


# In[48]:


GLD['change']= (GLD['high']/GLD['high'].shift(1))-1


# In[49]:


GLD.head(3)


# In[50]:


sum(GLD['change'][1:])


# In[51]:


SPY['change']= (SPY['high']/SPY['high'].shift(1))-1


# In[52]:


sum(SPY['change'][1:])


# In[53]:


def GLD_CHG(i): 
    C = GLD['high'][i]-GLD['low'][i]
    return(C)


# In[57]:


x = GLD_CHG(M)


# In[58]:


def GLD_DIF(i): 
    C = GLD['open'][i]-GLD['close'][i]
    return(C)


# In[59]:


y = GLD_DIF(M)


# In[61]:


plt.scatter(x, y)


# In[64]:


Metal = np.array([[[x],
                    [y],
                    [Gold]]])


# In[66]:


def SPY_CHG(i): 
    K = SPY['high'][i]-SPY['low'][i]
    return(K)


# In[67]:


def SPY_DIF(i): 
    L = SPY['open'][i]-SPY['close'][i]
    return(L)


# In[68]:


def VIX_CHG(i): 
    Q = VIX['high'][i]-VIX['low'][i]
    return(Q)


# In[69]:


def VIX_DIF(i): 
    W = VIX['open'][i]-VIX['close'][i]
    return(W)


# In[71]:


b = SPY_CHG(M)


# In[72]:


z = SPY_DIF(M)


# In[73]:


j = VIX_CHG(M)


# In[74]:


u = VIX_DIF(M)


# In[75]:


plt.scatter(b,z)


# In[76]:


plt.scatter(j,u)


# In[ ]:




