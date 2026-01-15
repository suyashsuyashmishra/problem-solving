#!/usr/bin/env python
# coding: utf-8

# In[1]:


import shapely


# In[2]:


from shapely import Point, LineString, Polygon, MultiPolygon


# # Top of the car
# 

# In[5]:


rectangle_1 = Polygon([(3,4),(5,4),(5,3),(3,3)])
rectangle_1


# ## Bottom of the car

# In[12]:


rectangle_2 = Polygon([(1,3),(6,3),(6,2),(1,2)])
rectangle_2


# In[26]:


point_1 = Point(1.5,1.5).buffer(0.5)
point_2 = Point(5.5,1.5).buffer(0.5)
multigeo = MultiPolygon([rectangle_1,rectangle_2,point_1,point_2])


# In[27]:


multigeo


# In[28]:


multigeo.area


# In[ ]:




