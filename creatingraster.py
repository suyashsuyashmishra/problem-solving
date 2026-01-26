#!/usr/bin/env python
# coding: utf-8

# In[90]:


import numpy as np


# ### Create single band raster data

# In[61]:


import rasterio


# In[63]:


num_rows, num_cols = 100, 100
one_band = np.random.rand(num_rows, num_cols)*255


# In[64]:


one_band


# In[67]:


one_data = one_band.astype(np.uint8)
one_data


# In[68]:


len(one_data)


# In[69]:


one_data[20][30]


# In[70]:


from rasterio.transform import from_origin
transform = from_origin(0,100,1,1)


# In[71]:


type(transform)


# In[81]:


meta = {
    'driver':'GTiff',
    'height':one_data.shape[0],
    'width' :one_data.shape[1],
    'count' :1,
    'dtype':one_data.dtype,
    'crs'   : 'EPSG:4326',
    'transform':transform
    
}


# In[82]:


meta


# In[83]:


with rasterio.open("single_band_raster.tif",'w',**meta) as dst:
    dst.write(one_data,1)


# In[84]:


import matplotlib.pyplot as plt
raster_file = "single_band_raster.tif"


# In[87]:


with rasterio.open(raster_file) as dataset:
    height = dataset.height
    width = dataset.width
    crs = dataset.crs
    dtype = dataset.dtypes[0]
    transform = dataset.transform
    number_bands = dataset.count
    band_data = dataset.read(1)
    


# In[89]:


plt.imshow(band_data, cmap = "Reds")
plt.colorbar(label = "Pixel_value")


# In[ ]:




