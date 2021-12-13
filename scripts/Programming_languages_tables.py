#!/usr/bin/env python
# coding: utf-8

# In[9]:


# Dependencies and Setup
import pandas as pd
from sqlalchemy import create_engine


# File path
seek_job_listing_path = r"C:\Users\Laurent\git\Project-2---ETL\Resources\listings2019_2021.csv"

# Read the job listing file
seek_job_listing = pd.read_csv(seek_job_listing_path)

# Display the job listing table 
seek_job_listing


# In[4]:


# Create a dataframe with jobId and programming languages of interest
programming_languages = seek_job_listing [['jobId', 'R', 'Python', 'Matlab', 'SQL', 'Ruby', 'C', 'Tableau', 'Java', 'Javascript']]

# Display programming languages dataframe 
programming_languages


# In[5]:


# Counting how many jobs require each specific language  
count_list = programming_languages[['R', 
                               'Python', 
                               'Matlab', 
                               'SQL', 
                               'Ruby', 
                               'C', 
                               'Tableau', 
                               'Java', 
                               'Javascript']].sum(axis=0)
count_list


# In[6]:


# Store the count into dataframe 
count_df = pd.DataFrame (count_list, columns = ['count of each programming language'])
count_df


# In[7]:


# Sorting counting in descending order 
count_df_ordered = count_df.sort_values('count of each programming language', ascending = False )
count_df_ordered


# # Loading dataframe into Postgres database

# In[13]:


#Creating connection to existing database


engine = create_engine('postgresql://postgres:postgres@localhost:5432/job_market_2019-2021')

# Deleting previous data and replacing with new data

engine.execute("delete from programming_languages") 
  
# Loading dataframe into existing database in Postgres

programming_languages.to_sql("programming_languages", engine, if_exists="append", index=False)


# In[ ]:




