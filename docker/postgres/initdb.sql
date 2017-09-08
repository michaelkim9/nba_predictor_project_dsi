CREATE DATABASE basketball;
\c basketball;

CREATE TABLE nba_draft (
    Draft_Year INTEGER
    Draft_Position INTEGER
    Draft_Team TEXT
    Player TEXT
    College TEXT
    Season_Count INTEGER
    G INTEGER
    MP INTEGER
    PTS INTEGER
    TRB INTEGER
    AST INTEGER
    FG_Perc FLOAT
    3P_Perc FLOAT
    FT_Perc FLOAT
    MP_1 FLOAT
    PTS_per_G FLOAT
    TRB_per_G FLOAT
    AST_per_G FLOAT
    WS FLOAT
    WS_per_48 FLOAT
    BPM FLOAT
    VORP FLOAT

\copy categories from '/docker-entrypoint-initdb.d/nba_draft.csv' with DELIMITER ',' CSV HEADER;


CREATE TABLE team_salary (
    Player TEXT
    Team TEXT
    2017-18 FLOAT
    2018-19 FLOAT
    2019-20 FLOAT
    2020-21 FLOAT
    2021-22 FLOAT
    2022-23 FLOAT
    Signed Using TEXT
    Guaranteed FLOAT

\copy pages from '/docker-entrypoint-initdb.d/team_salary.csv' with DELIMITER ',' CSV HEADER;



CREATE TABLE salary_cap (
    Year TEXT
    Salary_Cap FLOAT
    Salary_Cap_2015_Worth FLOAT

\copy pages from '/docker-entrypoint-initdb.d/salary_cap.csv' with DELIMITER ',' CSV HEADER;



CREATE TABLE nba_2016 (
    Player TEXT
    Position TEXT
    Shooting_Hand TEXT
    Height_inches FLOAT
    Weight_lbs FLOAT
    College TEXT
    Draft_Year INTEGER
    Draft_Position INTEGER
    Season_Count INTEGER
    Age INTEGER
    Current_Team TEXT
    G FLOAT
    GS FLOAT
    MP_per_G FLOAT
    PTS_per_G FLOAT
    FG_per_G FLOAT
    FGA_per_G FLOAT
    FG_Perc FLOAT
    3P_per_G FLOAT
    3PA_per_G FLOAT
    3P_Perc FLOAT
    2P_per_G FLOAT
    2PA_per_G FLOAT
    2P_Perc FLOAT
    EFG_Perc FLOAT
    FT_per_G FLOAT
    FTA_per_G FLOAT
    FT_Perc FLOAT
    ORB_per_G FLOAT
    DRB_per_G FLOAT
    TRB_per_G FLOAT
    AST_per_G FLOAT
    STL_per_G FLOAT
    BLK_per_G FLOAT
    TOV_per_G FLOAT
    PF_per_G FLOAT
    PER FLOAT
    WS FLOAT
    All_Star INTEGER
    Recent_Salary FLOAT
    Salary_Year INTEGER
    Salary_Team TEXT

\copy categories_pages from '/docker-entrypoint-initdb.d/nba_2016.csv' with DELIMITER ',' CSV HEADER;



CREATE TABLE nba_all_career (
    Player TEXT
    Position TEXT
    Shooting_Hand TEXT
    Height_inches FLOAT
    Weight_lbs FLOAT
    College TEXT
    Draft_Year INTEGER
    Draft_Position INTEGER
    Season_Count INTEGER
    Age INTEGER
    Current_Team TEXT
    G FLOAT
    GS FLOAT
    MP_per_G FLOAT
    PTS_per_G FLOAT
    FG_per_G FLOAT
    FGA_per_G FLOAT
    FG_Perc FLOAT
    3P_per_G FLOAT
    3PA_per_G FLOAT
    3P_Perc FLOAT
    2P_per_G FLOAT
    2PA_per_G FLOAT
    2P_Perc FLOAT
    EFG_Perc FLOAT
    FT_per_G FLOAT
    FTA_per_G FLOAT
    FT_Perc FLOAT
    ORB_per_G FLOAT
    DRB_per_G FLOAT
    TRB_per_G FLOAT
    AST_per_G FLOAT
    STL_per_G FLOAT
    BLK_per_G FLOAT
    TOV_per_G FLOAT
    PF_per_G FLOAT
    PER FLOAT
    WS FLOAT
    All_Star INTEGER
    Recent_Salary FLOAT
    Salary_Year INTEGER
    Salary_Team TEXT

\copy categories_pages from '/docker-entrypoint-initdb.d/nba_all_career.csv' with DELIMITER ',' CSV HEADER;





