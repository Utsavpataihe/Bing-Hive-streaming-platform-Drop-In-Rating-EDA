#!/usr/bin/env python
# coding: utf-8

# In[59]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[60]:


#read users_activity_log excel file 
user_activity = pd.read_csv("users_activity_log.csv")
user_activity


# In[61]:


#handling the null values


# In[62]:


user_activity.shape


# In[63]:


user_activity.isnull().sum()


# In[64]:


user_activity.dtypes


# In[65]:


user_activity["occurred_at"]=user_activity["occurred_at"].astype('datetime64[ns]')


# In[66]:


user_activity.dtypes


# In[67]:


#read device_details excel file 
device_details = pd.read_csv("device_details.csv")
device_details


# In[68]:


#handling the null values


# In[69]:


device_details.shape


# In[70]:


device_details.isnull().sum()


# In[71]:


#dropping null values
device_details1 = device_details.dropna()


# In[72]:


device_details1.isnull().sum()


# In[ ]:





# In[57]:


# saving the dataframe
user_activity.to_csv('user_activity_P_bi.csv')


# In[73]:


device_details1.to_csv('device_details1_P_bi.csv')


# In[34]:


# Get the type of devices that are affected by the issue.
device_types = error_search_queries['device_id'].unique()

print('Type of devices that are affected by the issue:')
print(device_types)

# Create a bar chart of the number of users with search errors by device type
plt.bar(device_types, [len(error_search_queries[error_search_queries['device_id'] == device_type]) for device_type in device_types])
plt.xlabel('Device Type')
plt.ylabel('Number of Users')
plt.title('Number of Users with Search Errors by Device Type')
plt.show()


# In[30]:


# Get the OS versions that are affected by the issue.
os_versions = error_search_queries['os_version'].unique()

print('OS versions that are affected by the issue:')
print(os_versions)

# Create a bar chart of the number of users with search errors by OS version
plt.bar(os_versions, [len(error_search_queries[error_search_queries['os_version'] == os_version]) for os_version in os_versions])
plt.xlabel('OS Version')
plt.ylabel('Number of Users')
plt.title('Number of Users with Search Errors by OS Version')
plt.show()


# In[ ]:





# In[28]:


# Get the time of day when the issues are occurring.
time_of_day = error_search_queries['occurred_at'].dt.time

print('Time of day when the issues are occurring:')
print(time_of_day)

time_of_day = pd.to_datetime(user_activity['occurred_at'])

# Create a bar chart of the number of users with search errors by time of day
plt.hist(time_of_day)
plt.xlabel('Time of Day')
plt.ylabel('Number of Users')
plt.title('Number of Users with Search Errors by Time of Day')
plt.show()


# In[32]:


# Filter the data to only include search queries that resulted in error messages.
error_search_queries = user_activity[user_activity['event_name'] == 'query_result_0']

# Count the number of users who are experiencing issues with the search functionality.
number_of_users_with_issues = len(error_search_queries)

# Print the results.
print('Number of users who are experiencing issues with the search functionality:')
print(number_of_users_with_issues)

# Create a bar chart of the number of users with search errors.
plt.bar([1], number_of_users_with_issues)
plt.xlabel('Number of Users')
plt.ylabel('Number of Search Errors')
plt.title('Number of Users with Search Errors')
plt.show()


# In[ ]:





# In[53]:


pivot_table = user_activity.pivot_table(values='user_id', index='event_name', columns='occurred_at', aggfunc=len)


# In[56]:


pivot_table


# In[ ]:




