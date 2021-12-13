/*Creating table for Job Title*/

CREATE TABLE job_title(
	index SERIAL,
	jobId INT PRIMARY KEY,
	jobTitle VARCHAR(30) NOT NULL,
	jobRole VARCHAR(30) NOT NULL

);

SELECT * FROM job_title;

/* Data imported from job_title.csv */

/*Creating table for Programming Languages*/

DROP TABLE Programming_languages;

CREATE TABLE programming_languages(
	index SERIAL,
	jobId INT,
	R VARCHAR(30) NOT NULL,
	Python VARCHAR(30) NOT NULL,
	Matlab VARCHAR(30) NOT NULL,
	SQL VARCHAR(30) NOT NULL,
	Ruby VARCHAR(30) NOT NULL,
	C VARCHAR(30) NOT NULL,
	Tableau VARCHAR(30) NOT NULL,
	Java VARCHAR(30) NOT NULL,
	Javascript VARCHAR(30) NOT NULL,
	FOREIGN KEY (jobId) REFERENCES job_title(jobId)

);
	SELECT * FROM programming_languages;

/* Data imported from programming_languages.csv */


/*Creating table for State*/


CREATE TABLE state(
	index SERIAL,
	jobId INT,
	state VARCHAR(30) NOT NULL,
	FOREIGN KEY (jobId) REFERENCES job_title(jobId)
	
);

SELECT * FROM state;

/* Data imported from state.csv */


/*Creating table for work_type*/

CREATE TABLE work_type(
	index SERIAL,
	jobId INT,
	Industry VARCHAR(30) NOT NULL,
	Departments VARCHAR(30) NOT NULL,
	workType VARCHAR(30) NOT NULL,
	FOREIGN KEY (jobId) REFERENCES job_title(jobId)

);

SELECT * FROM work_type;

/* Data imported from work_type.csv */
