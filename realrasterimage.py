#!/usr/bin/env python
# coding: utf-8

# In[91]:


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

input_data = "global_population_data
# ### For multiband dataset

# In[93]:


red_data= np.random.rand(num_rows,num_cols)*255
green_data= np.random.rand(num_rows,num_cols)*255
blue_data= np.random.rand(num_rows,num_cols)*255


# In[94]:


red_data = red_data.astype(np.uint8)
green_data = green_data.astype(np.uint8)
blue_data = blue_data.astype(np.uint8)


# In[96]:


rgb_data = np.stack([red_data,green_data,blue_data], axis= -1)


# In[97]:


rgb_data


# In[98]:


rgb_data[0][10]


# In[100]:


plt.imshow(rgb_data)


# #### Use real data for raster analysis

# In[103]:





# In[139]:


from rasterio.plot import show
raster_file = "D:\GeospatialAnalysis/GHS_SMOD_E2025_GLOBE_R2023A_54009_1000_V2_0.tif"
with rasterio.open(raster_file) as src:
    one_band = src.read(1, window=window, masked=True)
    values = one_band.compressed()
      

    



# In[116]:





# In[140]:





# In[141]:


import matplotlib.colors as colors
plt.imshow(one_band, cmap = 'Purples',
          norm = colors.LogNorm(vmin = one_band.min(), vmax = one_band.max()))
plt.title("Raster Visualization")
plt.xlabel('Pixel X')
plt.ylabel('Pixel Y')
plt.colorbar(label = 'Pixel Value')
plt.show()


# In[ ]:




