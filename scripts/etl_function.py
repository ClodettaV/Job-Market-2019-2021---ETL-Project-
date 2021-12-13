import pandas as pd
from pandas.core.frame import DataFrame

def my_function(input_df):
    job_role_df = input_df.copy(deep=True)


    job_role_df['jobTitle']=job_role_df['jobTitle'].str.lower()
    job_role_df.loc[job_role_df['jobTitle'].str.contains('engineer'), 'jobRole'] = 'Data Engineer'
    job_role_df.loc[job_role_df['jobTitle'].str.contains('developer'), 'jobRole'] = 'Data Engineer'
    job_role_df.loc[job_role_df['jobTitle'].str.contains('analyst'), 'jobRole'] = 'Data Analyst'
    job_role_df.loc[job_role_df['jobTitle'].str.contains('analytics'), 'jobRole'] = 'Data Analyst'
    job_role_df.loc[job_role_df['jobTitle'].str.contains('scientist'), 'jobRole'] = 'Data Scientist'
    job_role_df.loc[job_role_df['jobTitle'].str.contains('analyst/scientist'), 'jobRole'] = 'Data Scientist'
    job_role_df.loc[job_role_df['jobTitle'].str.contains('science'), 'jobRole'] = 'Data Scientist'


    return job_role_df
    