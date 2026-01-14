#!/usr/bin/env python
# coding: utf-8

# In[1]:


import shapely


# In[4]:


shapely.__version__


# In[5]:


from shapely import Point, LineString, Polygon, MultiPolygon


# ### Creating a point

# In[6]:


point = Point(0,0)


# In[7]:


type(point)


# In[8]:


point


# In[9]:


print(point)


# ### Creating a Linestring

# In[11]:


point_1 = Point(0,0)
point_2 = Point(1.5,1.5)
point = (point_1,point_2)


linestring = LineString(point)


# In[19]:


linestring


# In[21]:


print(linestring)
linestring.length


# ### Creating a Polygon

# In[23]:


point_1 = Point(0,0)
point_2 = Point(0,1)
point_3 = Point(1,1)
point_4 = Point(1,0)

point = (point_1,point_2,point_3,point_4)
polygon = Polygon(point)


# In[24]:


type(polygon)


# In[25]:


polygon


# In[26]:


print(polygon)


# In[27]:


polygon.area


# In[28]:


polygon.length


# #### Creating a MultiGeometries
# 

# In[37]:


square = Polygon([(0,0),(0,1),(1,1),(1,0)])

triangle = Polygon([(1,0),(1,1),(2,0)])

triangle


# In[33]:


square


# In[39]:


multigeo = MultiPolygon([square, triangle])
print(type(multigeo))


# In[40]:


multigeo


# In[41]:


multigeo.length


# In[42]:


multigeo.area


# In[ ]:




