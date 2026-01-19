#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np


# In[5]:


num_rows, num_cols = 100,100


# In[10]:


single_data =  np.random.rand(num_rows,num_cols)*255


# In[14]:


single_data = single_data.astype("uint8")
single_data


# In[15]:


single_data[0][0]


# In[17]:


red_data = np.random.rand(num_rows,num_cols)*255
blue_data = np.random.rand(num_rows,num_cols)*255
green_data = np.random.rand(num_rows,num_cols)*255


# In[19]:


rgb_data = np.stack([red_data, green_data, blue_data], axis = -1).astype(np.uint8)


# In[20]:


rgb_data


# In[ ]:




