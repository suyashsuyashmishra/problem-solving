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


# ### Geometrics Operation

# In[51]:


point  = Point(0,0)
point.buffer(1.2)

linestring.buffer(0.2)
multige


# In[53]:


triangle.buffer(0.2)


# ### Buffer is a way to convert any geomtry into the polygon .

# ## CENTROID
# 
# can turn any geometry into center point

# In[55]:


line_center = linestring.centroid


# In[56]:


line_center


# In[58]:


triangle_center = triangle.centroid


# In[59]:


triangle_center


# ## COVEX HULL
# 
# create smallest possible convex and closing polygon around geometry

# In[66]:


line = LineString([(0,0),(0,1),(1,1)])


# In[67]:


line


# In[69]:


line.convex_hull


# In[70]:


line.buffer(0.2)


# In[71]:


line.buffer(0.2).convex_hull


#   ## SET OPEARATION IN GEOMETRICS

# In[72]:


circle_1 = Point(0,0).buffer(2.0)
circle_2 = Point(3,0).buffer(2.0)


# In[73]:


circle_1.union(circle_2)


# In[75]:


circle_1.intersection(circle_2)


# In[76]:


circle_1.difference(circle_2)


# In[79]:


circle_2.difference(circle_1)


# ## Within Command

# In[80]:


new_point = Point(0,0)


# In[86]:


triangle_1 = Polygon([(0,-1),(-1,1),(2,0)])


# In[83]:


triangle_2 = Polygon([(3,4),(5,7),(5,1)])


# In[84]:


triangle_2


# In[87]:


new_point.within(triangle_1)


# In[89]:


new_point.within(triangle_2)


# In[90]:


new_point.union(triangle_1).union(triangle_2)


# ## Distance Measurement

# Distance measurement is done using shapely library

#  measuring the distance between previous identified points. Units depend on the cocordinate system of the data

# In[92]:


new_point.distance(triangle_1)


# In[93]:


new_point.distance(triangle_2)


# In[ ]:




