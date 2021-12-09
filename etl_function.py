import pandas as pd

def my_function(input_df):
    job_role_df = input_df.copy(deep=True)

    job_role_df['jobTitle']=job_role_df['jobTitle'].str.lower()
    job_role_df.loc[job_role_df['jobTitle'].str.contains('engineer'), 'jobRole'] = 'Data Engineer'
    job_role_df.loc[job_role_df['jobTitle'].str.contains('analyst'), 'jobRole'] = 'Data Analyst'
    job_role_df.loc[job_role_df['jobTitle'].str.contains('scientist'), 'jobRole'] = 'Data Scientist'
    job_role_df.loc[job_role_df['jobTitle'].str.contains('analyst/scientist'), 'jobRole'] = 'Data Scientist'

    return job_role_df
    