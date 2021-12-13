#!/usr/bin/env python
# coding: utf-8

# In[21]:


#import dependencies
import pandas as pd
import numpy as np
import psycopg2
from sqlalchemy import create_engine



# In[22]:


#load in file
file_path = r"C:\Users\Laurent\git\Project-2---ETL\Resources\listings2019_2021.csv"


# Reading the file from csv

# In[23]:


summary_df = pd.read_csv(file_path)
summary_df.head()


# Creating a table for States

# In[24]:


#creating a required table
state_df = summary_df[["jobId","state"]]
state_df
            
                           


# Creating a table for work type by using appropriate columns

# In[25]:


work_type = summary_df[["jobId","jobClassification","jobSubClassification","workType"]]
work_type


# Renaming the columns

# In[26]:


work_type = work_type.rename(columns={"jobClassification": "Industry", "jobSubClassification": "Departments"})
work_type


# # Loading dataframe into Postgres database

# In[29]:


#Creating connection to existing database


engine = create_engine('postgresql://postgres:postgres@localhost:5432/job_market_2019-2021')

# Deleting previous data and replacing with new data

engine.execute("delete from state") 
  
# Loading dataframe into existing database in Postgres

state_df.to_sql("state", engine, if_exists="append", index=False)


# In[28]:


# Loading second table inside the database

engine = create_engine('postgresql://postgres:postgres@localhost:5432/job_market_2019-2021')

# Deleting previous data and replacing with new data

engine.execute("delete from work_type") 
  
# Loading dataframe into existing database in Postgres

work_type.to_sql("work_type", engine, if_exists="append", index=False)


# In[ ]:




