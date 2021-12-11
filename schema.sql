/*Creating table for Job Title*/

CREATE TABLE job_title(
	jobiD INT,
	jobTitle VARCHAR,
	jobRole VARCHAR

);

SELECT * FROM job_title;

/*Creating table for Programming Languages*/

DROP TABLE Programming_languages;

CREATE TABLE programming_languages(
	
	index SERIAL,
	jobiD INT,
	R VARCHAR,
	Python VARCHAR,
	Matlab VARCHAR,
	SQL VARCHAR,
	Ruby VARCHAR,
	C VARCHAR,
	Tableau VARCHAR,
	Java VARCHAR,
	Javascript VARCHAR
);
	SELECT * FROM programming_languages;

/*Creating table for State*/


CREATE TABLE state(
	index INT,
	jobId VARCHAR,
	state VARCHAR	
);

SELECT * FROM state;

/*Creating table for work_type*/

CREATE TABLE work_type(
	index INT,
	jobId VARCHAR,
	Industry VARCHAR,
	Departments VARCHAR,
	workType VARCHAR
);

SELECT * FROM work_type;

