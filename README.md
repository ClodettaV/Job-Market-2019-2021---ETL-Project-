# Project-2 - ETL

**Purpose and Motivation**

The aim of this project is to assist data analysts in accessing data regarding the 
job market for data science from 2019 to 2021. This will enable data analysts to 
analyse the job requirements and prospects in several areas in Australia. The 
data were sourced from seek.com, one of the leading recruitment platforms in 
Australia. The raw data have been transformed and normalised into meaningful 
set of tables using Pandas on Jupyter notebook and loaded into PostgreSQL 
database.

This code repository contains the solution to perform the ETL on a scheduled 
basis and stores the data in a PostgreSQL Database.

Unit tests have been performed to assure transformation and normalisation has been properly executed.

**Repo structure**

![image](https://user-images.githubusercontent.com/88511756/145743819-c50b7a81-1360-46fd-a1b6-ed8fe95be151.png)

**ERD and Data Dictionary**

Entity Relationship Diagram
The ERD diagram was created using: https://app.quickdatabasediagrams.com/#/

![image](https://user-images.githubusercontent.com/88511756/145743861-4ed8e059-e5b4-40b9-920a-9e279ebe3db5.png)

**Data dictionary**

Below are the data definitions for the following tables:

Job Title
Column name	Definition
JobId	The unique ID for the job
jobTitle	The title of each job
jobRole	Broader job title

Programming languages
Column name	Definition
jobId	The unique ID for the job
R	Programming language either required (1) or not(0) for each job
Matlab	Programming language either required (1) or not(0) for each job
Python	Programming language either required (1) or not(0) for each job
Kavascript	Programming language either required (1) or not(0) for each job
SQL	Programming language either required (1) or not(0) for each job
Tableau	Programming language either required (1) or not(0) for each job
C	Programming language either required (1) or not(0) for each job
Java	Programming language either required (1) or not(0) for each job
Ruby	Programming language either required (1) or not(0) for each job

State
Column name	Definition
jobId	The unique ID for the job
state	The state where the job is based 

Work Type
Column name	Definition
jobId	The unique ID for the job
Industry	The renamed job classification
Departments	The renamed job sub-classification
Works_type	The type of contract


Usage
The required python libraries and version are 

	
•	Python dependencies
•	pandas==1.3.2
	•	sqlalchemy==1.4.26
	•	pytest==6.2.5

Install python dependencies by performing:
pip install -r 
Running code locally
Run unit tests
Scheduling jobs

**Contributors**
@ClodettaV
@Lau-518
@MonikaSidhu1
