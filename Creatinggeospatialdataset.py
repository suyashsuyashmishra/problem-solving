#!/usr/bin/env python
# coding: utf-8

# In[14]:


import geopandas as gpd
from shapely.geometry import Point, Polygon
import matplotlib.pyplot as plt


# In[15]:


top = Polygon([(0, 1), (0, 2), (2, 2), (2, 1)])
bottom = Polygon([(-1, 0), (-1, 1), (4, 1), (4, 0)])
wheel_front = Point(0, -0.5).buffer(0.5)
wheel_rear = Point(3, -0.5).buffer(0.5)


# In[16]:


geometries = [top, bottom, wheel_front, wheel_rear]
geometries


# In[17]:


gdf = gpd.GeoDataFrame(geometry=geometries)
gdf.crs = 4326
display(gdf)


# In[22]:


gdf['geometry_length'] = gdf.length
gdf['geometry_area'] = gdf.area
gdf.head()


# In[23]:


gdf['geometry'] = [g.buffer(0.2) for g in gdf.geometry.to_list()]
gdf.head()


# In[24]:


f, ax = plt.subplots(1, 1, figsize=(7, 7))

gdf.plot(column='geometry_length', ax=ax, cmap='Reds', edgecolor='steelblue', linewidth=2, alpha=0.8)


# In[25]:


gdf_nyc = gdf.to_crs(2263)
gdf_hun = gdf.to_crs(23700)


# In[27]:


f, ax = plt.subplots(1, 2, figsize=(7, 7))
gdf_nyc.plot(column='geometry_length', ax=ax[0], cmap='Reds', edgecolor='steelblue', linewidth=2, alpha=0.8, legend = True)
gdf_hun.plot(column='geometry_length', ax=ax[1], cmap='Blues', edgecolor='steelblue', linewidth=2, alpha=0.8, legend = True)

plt.show()


# In[ ]:




