import pandas as pd
from etl_function import *

def test_my_function():

    # ASSEMBLE 
    input_df = pd.DataFrame({
        "id": [1,2],
        "jobtitle1": ["Business Analyst","POWERbi ANALYST"], 
        "jobtitle2": ["data scientist","data scientist/data analyst"]
    })

    expected_df = pd.DataFrame({
        "id": [1,2], 
        "jobtitle1": ["Data Analyst", "Data Analyst"], 
        "jobtitle2": ["Data Scientist", "Data Scientist"]
    })

    # ACT 
    # output_df = my_function(input_df=input_df, Job_role=["jobtitle1", "jobtitle2"])
    # output_df = my_function(input_df=input_df, job_role_df=["jobtitle1", "jobtitle2"])
    output_df = my_function(input_df=input_df)


    # ASSERT 

    pd.testing.assert_frame_equal(left=output_df, right=expected_df,check_exact=True)

