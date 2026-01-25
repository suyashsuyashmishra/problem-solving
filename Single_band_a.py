#!/usr/bin/env python
# coding: utf-8

# In[49]:


import numpy as np
import matplotlib.pyplot as plt


# In[55]:


num_rows, num_cols = 20,20
single_data = np.zeros((num_rows,num_cols), dtype = (np.uint8))
single_data[5:15,5] = 1
single_data[5:15,14] = 1

single_data[5,5:15] = 1
single_data[10,5:15] = 1
single_data = single_data*255


# In[56]:


plt.imshow(single_data, cmap = 'gray')
plt.title("Singel band dataset of A")
plt.show()


# In[ ]:




