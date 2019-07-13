#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')
import pandas
import seaborn


# In[3]:


data = pandas.read_csv('Desktop/uber-raw-data-apr14.csv')


# In[4]:


data


# In[5]:


data.tail()


# # Convert datetime and add some useful columns¶

# In[9]:


data['Date/Time'] = data['Date/Time'].map(pandas.to_datetime)


# In[10]:


data.tail()


# In[11]:


def get_dom(dt):
    return dt.day

data['dom'] = data['Date/Time'].map(get_dom)


# In[12]:


data.tail()


# In[13]:


def get_weekday(dt):
    return dt.weekday()

data['weekday'] = data['Date/Time'].map(get_weekday)

def get_hour(dt):
    return dt.hour

data['hour'] = data['Date/Time'].map(get_hour)

data.tail()


# # ANALYSIS

# # analyze the DoM

# In[15]:


hist(data.dom, bins=30, rwidth=.8, range=(0.5, 30.5))
xlabel('date of the month')
ylabel('frequency')
title('Frequency by DoM - uber - Apr 2014')


# In[16]:


#for k, rows in data.groupby('dom'):
#    print((k, len(rows)))
 
def count_rows(rows):
    return len(rows)

by_date = data.groupby('dom').apply(count_rows)
by_date


# In[17]:


bar(range(1, 31), by_date)


# In[18]:


by_date_sorted = by_date.sort_values()
by_date_sorted


# In[19]:


bar(range(1, 31), by_date_sorted)
xticks(range(1,31), by_date_sorted.index)
xlabel('date of the month')
ylabel('frequency')
title('Frequency by DoM - uber - Apr 2014')
("")


# # analyze the hour¶
# 

# In[22]:


hist(data.hour, bins=24, range=(.5, 24))


# # analyze the weekday

# In[23]:


hist(data.weekday, bins=7, range =(-.5,6.5), rwidth=.8, color='#AA6666', alpha=.4)
xticks(range(7), 'Mon Tue Wed Thu Fri Sat Sun'.split())


# # cross analysis (hour, dow)

# In[24]:


by_cross = data.groupby('weekday hour'.split()).apply(count_rows).unstack()


# In[25]:


seaborn.heatmap(by_cross)


# # by lat and lon

# In[26]:


hist(data['Lat'], bins=100, range = (40.5, 41))
("")


# In[27]:


hist(data['Lon'], bins=100, range = (-74.1, -73.9));


# In[28]:



hist(data['Lon'], bins=100, range = (-74.1, -73.9), color='g', alpha=.5, label = 'longitude')
grid()
legend(loc='upper left')
twiny()
hist(data['Lat'], bins=100, range = (40.5, 41), color='r', alpha=.5, label = 'latitude')
legend(loc='best')
("")


# In[29]:


figure(figsize=(20, 20))
plot(data['Lon'], data['Lat'], '.', ms=1, alpha=.5)
xlim(-74.2, -73.7)
ylim(40.7, 41)


# In[ ]:




