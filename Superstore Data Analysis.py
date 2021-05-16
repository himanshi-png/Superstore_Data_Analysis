#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Importing libraries
# import numpy as np import pandas as pd import seaborn as sns import matplotlib.pyplot as plt %matplotlib inline


# In[3]:


import pandas as pd
df_raw=pd.read_csv("SampleSuperstore.csv")


# In[4]:


# Data Preparation and Cleaning


# In[5]:


df_raw.head(10)


# In[6]:


# Summary of data
df_raw.isnull()


# In[7]:


df_raw.describe()


# In[8]:


df_raw.info()


# In[9]:


# Exploratory Analysis and Visualisation


# In[10]:


# TODO-Which region has least sales?


# In[13]:


import seaborn as sns
import matplotlib.pyplot as plt
lowest_sales_region = df_raw.groupby('Region')['Sales'].sum().sort_values(ascending=True).head()
lowest_sales_region = lowest_sales_region.reset_index()
sns.set_context('talk')
plt.figure(figsize=(30,6));
plt.title('Region wise Sales', fontweight='bold', fontsize=25);

plt.xlabel('Region', fontweight='bold')
plt.ylabel('Sales', fontweight='bold')

# Displaying the Sales amount for each Customer
for i, v in enumerate(lowest_sales_region['Sales'].tolist()):
    plt.text(v+5, i + .1 , '$' + str(round(int(v)/1000)) + 'k', color='Black', fontweight='bold')


sns.barplot( 'Sales','Region', data=lowest_sales_region);


# In[14]:


# TODO- How are the sales of each category is divided across the regions?


# In[15]:


category_df = pd.pivot_table(df_raw,index=['Category'], columns=['Region'], values=['Sales'], aggfunc='sum')
category_df.plot.barh(stacked=True);
plt.title('Category Sales in each region vs Sales', fontweight='bold', fontsize=10);

plt.xlabel('Sales', fontweight='bold')
plt.ylabel('Category', fontweight='bold')


# In[16]:


# TODO- How are the Sales across each segment?


# In[18]:


import numpy as np
df_raw.Profit=np.where(df_raw.Profit<0,0,df_raw.Profit)
#Displaying Sales of each segment
plt.bar(df_raw.Segment,df_raw.Sales);
plt.title('Sales vs Segment')
plt.xlabel('Segment')
plt.ylabel('Sales')


# In[20]:


# TODO- Which State has the lowest sales?


# In[21]:


lowest_revenue_states = df_raw.groupby('State')['Sales'].sum().sort_values(ascending=True).head(10)

lowest_revenue_states = lowest_revenue_states.reset_index()
sns.set_context('talk')
sns.set_style('darkgrid')
plt.figure(figsize=(28,10))
plt.title('Lowest 10 States which generated lowest sales' , fontweight='bold', fontsize=25);
plt.xlabel('Sales', fontweight='bold')
plt.ylabel('State', fontweight='bold')

# Displaying the Sales amount for each State 
for i, v in enumerate(lowest_revenue_states['Sales'].tolist()):
    plt.text(v+5, i + .1 , '$' + str(round(int(v)/1000)) + 'k', color='Black', fontweight='bold')

sns.barplot(lowest_revenue_states['Sales'], lowest_revenue_states['State']);


# In[23]:


# TODO- Which city has least sales?


# In[24]:


lowest_revenue_cities = df_raw.groupby('City')['Sales'].sum().sort_values(ascending=True).head(10)

lowest_revenue_cities = lowest_revenue_cities.reset_index()
sns.set_context('talk')
sns.set_style('darkgrid')
plt.figure(figsize=(28,20))
plt.title('Lowest 10 cities which generated the least sales' , fontweight='bold', fontsize=25);
plt.xlabel('Sales', fontweight='bold')
plt.ylabel('City', fontweight='bold')

# Displaying the Sales amount for top 10 Cities 
for i, v in enumerate(lowest_revenue_cities['Sales'].tolist()):
    plt.text(v+5, i + .1 , '$' + str(round(int(v)/1000)) + 'k', color='Black', fontweight='bold')

sns.barplot(lowest_revenue_cities['Sales'], lowest_revenue_cities['City']);


# In[25]:


# Which is the lowest shipping mode?


# In[26]:


lowest_shipping_modes = df_raw['Ship Mode'].value_counts()
label_ship_mode = lowest_shipping_modes.index.tolist()
#Plotting Pie Chart
sns.set_context('talk');
plt.figure(figsize=(7,7));
plt.pie(lowest_shipping_modes, explode=(0.01,0.005,0.01, 0.01), labels=label_ship_mode, autopct='%1.0f%%', shadow=False, colors=['darkorange', 'mediumslateblue', 'mediumvioletred', 'green'] , startangle=45);
plt.axis('equal');
plt.title('Lowest Shipping Mode', fontweight='bold', fontsize=25);

