CREATE TABLE title_crew (
	tconst TEXT PRIMARY KEY,
	directors TEXT,
	writers TEXT
);
    
CREATE TABLE name_basics ( nconst TEXT PRIMARY KEY,
	primaryname TEXT,
	birthyear TEXT,
	deathyear TEXT,
    primaryprofession TEXT,
    knownfortitles TEXT
);
   
CREATE TABLE title_basics ( tconst TEXT PRIMARY KEY,
	titletype TEXT,
	primarytitle TEXT,
	originaltitle TEXT,
    isadult TEXT,
    startyear TEXT,
   endyear TEXT,
   runtimeminutes TEXT,
   genres TEXT
);
   
   
CREATE TABLE title_episodes ( tconst TEXT PRIMARY KEY,
	parenttconst TEXT,
	seasonnumber INT,
	epiodenumber INT
);
    
    
CREATE TABLE title_ratings ( tconst TEXT PRIMARY KEY,
	averagerating REAL,
	numvotes INT
);


CREATE TABLE title_principals ( tconst TEXT PRIMARY KEY,
	ordering INT
	nconst TEXT,
	category TEXT,
    job TEXT,
    characters TEXT,
 CONSTRAINT fk_nconst
    FOREIGN KEY nconst
    REFERENCES name_basics(nconst)
);


CREATE TABLE title_akas ( titleid TEXT PRIMARY KEY,
	ordering INT
	title TEXT,
	region TEXT,
    language TEXT,
    types TEXT,
    attributes TEXT,
    isoriginaltitle TEXT
);