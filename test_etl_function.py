import pandas as pd
from etl_function import *

def test_my_function():

    # ASSEMBLE 
    input_df = pd.DataFrame({
        "id": [1,2,3,4],
        "jobTitle": ["Business Analyst","POWERbi ANALYST", "data scientist","data scientist/data analyst"],
        "jobRole": ["", "","", ""]

    })

    expected_df = pd.DataFrame({
        "id": [1,2,3,4],
        "jobTitle": ["business analyst","powerbi analyst", "data scientist","data scientist/data analyst"],
        "jobRole": ["Data Analyst", "Data Analyst","Data Scientist", "Data Scientist"]
    })

    # ACT 
    # output_df = my_function(input_df=input_df, Job_role=["jobtitle1", "jobtitle2"])
    # output_df = my_function(input_df=input_df, job_role_df=["jobtitle1", "jobtitle2"])
    output_df = my_function(input_df=input_df)


    # ASSERT 

    pd.testing.assert_frame_equal(left=output_df, right=expected_df,check_exact=True)

