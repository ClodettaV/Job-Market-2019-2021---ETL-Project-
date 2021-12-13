#!/usr/bin/env python
# coding: utf-8

# # Importing dependencies

# In[8]:


#import dependencies

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from etl_function import *
import psycopg2
from sqlalchemy import create_engine


# # Extracting data from CSV file

# In[13]:


# Load in file
file_path = r"C:\Users\Laurent\git\Project-2---ETL\Resources\listings2019_2021.csv"


# In[14]:


# Read and display the CSV with Pandas

summary_df = pd.read_csv(file_path,encoding='ISO-8859-1')
summary_df.head()


# # Transforming data (Normalise - filtering)

# In[15]:


#Selecting wanted columns

job_role_df = summary_df[["jobId","jobTitle"]]
job_role_df


# In[16]:


#Adding new col - job role

job_role_df["jobRole"] = ""
job_role_df


# Calling function to filter through dataframe

# In[17]:


#Calling function


jobs_per_role =  my_function(job_role_df)
jobs_per_role


# In[18]:


#deleting blank rows in Job Role column

jobs_per_role = jobs_per_role.drop(jobs_per_role[jobs_per_role.jobRole == ""].index)


# In[19]:


jobs_per_role


# # Count per job role (new table created)

# In[ ]:


job_role_counts = jobs_per_role["jobRole"].value_counts()
job_role_counts


# In[ ]:


count_df = pd.DataFrame (job_role_counts, columns = ['jobRole'])
count_df


# # Loading dataframe into Postgres database

# In[25]:


#Creating connection to existing database


engine = create_engine('postgresql://postgres:postgres@localhost:5432/job_market_2019-2021')

# Deleting previous data and replacing with new data

engine.execute("delete from job_title") 
  
# Loading dataframe into existing database in Postgres

jobs_per_role.to_sql("job_title", engine, if_exists="append", index=False)


# In[ ]:




