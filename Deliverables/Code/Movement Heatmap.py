#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import plotly.express as px


# In[2]:


park_movement_Fri = pd.read_csv("park-movement-Fri.csv")
park_movement_Sat = pd.read_csv("park-movement-Sat.csv")
park_movement_Sun = pd.read_csv("park-movement-Sun.csv")


# In[3]:


park_movement_Sun = park_movement_Sun.drop(park_movement_Sun.index[-1])

park_movement_Fri["datetime"] = pd.to_datetime(park_movement_Fri["Timestamp"])
park_movement_Fri["time_h"] = park_movement_Fri["datetime"].dt.strftime("%m-%d %H")
park_movement_Sat["datetime"] = pd.to_datetime(park_movement_Sat["Timestamp"])
park_movement_Sat["time_h"] = park_movement_Sat["datetime"].dt.strftime("%m-%d %H")
park_movement_Sun["datetime"] = pd.to_datetime(park_movement_Sun["Timestamp"])
park_movement_Sun["time_h"] = park_movement_Sun["datetime"].dt.strftime("%m-%d %H")


# In[4]:


park_movement_Sun = park_movement_Sun.dropna(subset=['type'])
park_movement_Sun.head()


# In[5]:


binplot_Fri = px.density_heatmap(park_movement_Fri, x = "X", y = "Y", animation_frame = "time_h", facet_col = "type", range_x = [0, 99], range_y = [0, 99])
binplot_Fri.show()


# In[6]:


binplot_Sat = px.density_heatmap(park_movement_Sat, x = "X", y = "Y", animation_frame = "time_h", facet_col = "type", range_x = [0, 99], range_y = [0, 99])
binplot_Sat.show()


# In[7]:


binplot_Sun = px.density_heatmap(park_movement_Sun, x = "X", y = "Y", animation_frame = "time_h", facet_col = "type", range_x = [0, 99], range_y = [0, 99])
binplot_Sun.show()


# In[ ]:




