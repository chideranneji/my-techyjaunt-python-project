#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn


# In[2]:


df = pd.read_csv("Amazon Sale Report.csv",low_memory=False)


# In[3]:


df.head(60)


# In[4]:


df.info()


# In[5]:


df.isnull().sum()


# In[6]:


df.describe(include="all")


# In[7]:


#checking the mode_value for the entire data frame
mode_df = df.mode()


# In[8]:


#print(mode_df)


# In[9]:


# For a specific column, e.g., 'column_name'
mode_value = df['Courier Status'].mode()


# In[10]:


print(mode_value)


# In[11]:


# For a specific column, e.g., 'column_name'
mode_value = df['currency'].mode()


# In[12]:


print(mode_value)


# In[13]:


# For a specific column, e.g., 'column_name'
mode_value = df['Amount'].mode()


# In[14]:


print(mode_value)


# In[15]:


# For a specific column, e.g., 'column_name'
mode_value = df['ship-city'].mode()


# In[16]:


print(mode_value)


# In[17]:


# For a specific column, e.g., 'column_name'
mode_value = df['ship-postal-code'].mode()


# In[18]:


print(mode_value)


# In[19]:


# For a specific column, e.g., 'column_name'
mode_value = df['ship-country'].mode()


# In[20]:


print(mode_value)


# In[21]:


# For a specific column, e.g., 'column_name'
mode_value = df['promotion-ids'].mode()


# In[22]:


print(mode_value)


# In[23]:


# Replace missing values with a specific value,for columns
df['Courier Status'].fillna('Shipped', inplace=True)
df['currency'].fillna('INR', inplace=True)
df['Amount'].fillna(0, inplace=True)
df['ship-city'].fillna('BENGALURU', inplace=True)
df['ship-state'].fillna('MAHARASHTRA', inplace=True)
df['ship-postal-code'].fillna(0, inplace=True)
df['ship-country'].fillna('IN', inplace=True)
df['promotion-ids'].fillna('IN Core Free Shipping 2015/04/08 23-48-5-108', inplace=True)


# In[24]:


df.info()


# In[25]:


df.drop(columns=['fulfilled-by'],inplace=True)


# In[26]:


df.drop(columns=['Unnamed: 22'],inplace=True)


# In[27]:


df.info()


# In[28]:


#to add another column named sales by multiplying quatity ordered by amount
df['Sales']=df['Qty']*df['Amount']


# In[29]:


df.head()


# In[30]:


#to check for the unique date
df['Date'].unique()


# In[31]:


#to split the into month
'4/15/2022'.split('/')[0:1]


# In[32]:


#to add another column called month
def Month(x):
    return x.split('/')[0]
df['Month'] = df['Date'].apply(Month)


# In[33]:


df.head()


# In[34]:


df.dtypes


# In[35]:


#to change the month data type from object to integer
df['Month']=df['Month'].astype(int)


# In[36]:


df.dtypes


# In[37]:


#to check the unique value of the month
df['Month'].unique()


# In[38]:


#the month with the highest sales
df.groupby('Month')['Sales'].sum()


# In[39]:


#to plot the graph with the month with the highest sales
months=range(1,5)
plt.bar(months,df.groupby('Month')['Sales'].sum(),color='blue')
plt.xticks(months)
plt.ylabel('Sales')
plt.xlabel('Month')
plt.show()


# In[40]:


#top 10 ship-state by quantity ordered
top_10_ship_state = df.sort_values(by='Qty', ascending=False).head(10)


# In[41]:


#visualize top 10 ship_state with the quantity orderd
plt.figure(figsize=(10,5))
plt.bar(top_10_ship_state['ship-state'],top_10_ship_state['Qty'],color='blue')
plt.ylabel('Quantity ordered')
plt.xlabel('state names')
plt.xticks(rotation='vertical')
plt.show()


# In[45]:


#top 10 city with the highest sales
plt.figure(figsize=(10,5))
plt.bar(top_10_ship_state['ship-city'],top_10_ship_state['Sales'],color='blue')
plt.ylabel('Sales')
plt.xlabel('City names')
plt.xticks(rotation='45')
plt.show()
           
           


# In[46]:


df['Status'].unique()


# In[47]:


#proportion of completed,pending,and canceled and other
df['Status'].value_counts(normalize=True).plot(kind='bar')


# In[48]:


#fulfillment statistical info
df['Fulfilment'].describe()


# In[49]:


#checking if quicker fulfullment correlate with higher sales
df.groupby('Fulfilment')['Sales'].sum().plot(kind='line')


# In[51]:


#Total revenue analysis

total_sales = df['Sales'].sum()
print('Total Sales: ',total_sales)


# In[53]:


#Average order value

avg_order_value=df['Sales'].mean()
print('Average Order Value: ',avg_order_value)


# In[54]:


#shows distribution of order sizes

df['Qty'].plot(kind='hist', bins=20)


# In[55]:


#visualize the most popular sizes among product

df['Size'].value_counts().plot(kind='bar')


# In[56]:


#shows the product categories that contribute most to sales.

df.groupby('Category')['Sales'].sum().sort_values(ascending=False).plot(kind='bar')


# In[57]:


#Analyzes the distribution of different courier statuses to understand delivery efficiency.

df['Courier Status'].value_counts().plot(kind='bar')


# In[58]:


#examine how courier performance affect order completion.

df.groupby('Courier Status')['Status'].value_counts(normalize=True).unstack().plot(kind='bar', stacked=True)


# In[59]:


#vistualize which categories has highest order

df.groupby('Category')['Qty'].sum().plot(kind='bar')


# In[ ]:




