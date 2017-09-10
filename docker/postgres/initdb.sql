CREATE DATABASE basketball;
\c basketball;

CREATE TABLE nba_draft (
    Draft_Year INTEGER,
    Draft_Position INTEGER,
    Draft_Team TEXT,
    Player TEXT,
    College TEXT,
    Season_Count INTEGER,
    G INTEGER,
    MP INTEGER,
    PTS INTEGER,
    TRB INTEGER,
    AST INTEGER,
    FG_Perc FLOAT,
    Three_Perc FLOAT,
    FT_Perc FLOAT,
    MP_1 FLOAT,
    PTS_per_G FLOAT,
    TRB_per_G FLOAT,
    AST_per_G FLOAT,
    WS FLOAT,
    WS_per_48 FLOAT,
    BPM FLOAT,
    VORP FLOAT);

\copy nba_draft from '/docker-entrypoint-initdb.d/nba_draft.csv' with DELIMITER ',' CSV HEADER;

CREATE TABLE team_salary (
    Player TEXT,
    Team TEXT,
    Year_Zero FLOAT,
    Year_One FLOAT,
    Year_Two FLOAT,
    Year_Three FLOAT,
    Year_Four FLOAT,
    Year_Five FLOAT,
    Signed_Using TEXT,
    Guaranteed FLOAT);

\copy team_salary from '/docker-entrypoint-initdb.d/team_salary.csv' with DELIMITER ',' CSV HEADER;

CREATE TABLE salary_cap (
    Year TEXT,
    Salary_Cap FLOAT,
    Salary_Cap_2015_Worth FLOAT);

\copy salary_cap from '/docker-entrypoint-initdb.d/salary_cap.csv' with DELIMITER ',' CSV HEADER;

CREATE TABLE nba_2016 (
    Player TEXT,
    Position TEXT,
    Shooting_Hand TEXT,
    Height_inches FLOAT,
    Weight_lbs FLOAT,
    College TEXT,
    Draft_Year INTEGER,
    Draft_Position INTEGER,
    Season_Count INTEGER,
    Age INTEGER,
    G FLOAT,
    GS FLOAT,
    MP FLOAT,
    FG FLOAT,
    FGA FLOAT,
    FG_Perc FLOAT,
    Three_P FLOAT,
    Three_Att FLOAT,
    Three_Perc FLOAT,
    Two_P FLOAT,
    Two_Att FLOAT,
    Two_Perc FLOAT,
    EFG_Perc FLOAT,
    FT FLOAT,
    FTA FLOAT,
    FT_Perc FLOAT,
    ORB FLOAT,
    DRB FLOAT,
    TRB FLOAT,
    AST FLOAT,
    STL FLOAT,
    BLK FLOAT,
    TOV FLOAT,
    PF FLOAT,
    PTS FLOAT,
    All_Star INTEGER,
    PER FLOAT,
    WS FLOAT,
    Salary FLOAT);

\copy nba_2016 from '/docker-entrypoint-initdb.d/nba_2016.csv' with DELIMITER ',' CSV HEADER;

CREATE TABLE nba_all_career (
    Player TEXT,
    Position TEXT,
    Shooting_Hand TEXT,
    Height_inches FLOAT,
    Weight_lbs FLOAT,
    College TEXT,
    Draft_Year INTEGER,
    Draft_Position INTEGER,
    Season_Count INTEGER,
    Age INTEGER,
    Current_Team TEXT,
    G FLOAT,
    GS FLOAT,
    MP_per_G FLOAT,
    PTS_per_G FLOAT,
    FG_per_G FLOAT,
    FGA_per_G FLOAT,
    FG_Perc FLOAT,
    Three_per_G FLOAT,
    Three_Att_per_G FLOAT,
    Three_Perc FLOAT,
    Two_per_G FLOAT,
    Two_Att_per_G FLOAT,
    Two_Perc FLOAT,
    EFG_Perc FLOAT,
    FT_per_G FLOAT,
    FTA_per_G FLOAT,
    FT_Perc FLOAT,
    ORB_per_G FLOAT,
    DRB_per_G FLOAT,
    TRB_per_G FLOAT,
    AST_per_G FLOAT,
    STL_per_G FLOAT,
    BLK_per_G FLOAT,
    TOV_per_G FLOAT,
    PF_per_G FLOAT,
    All_Star INTEGER,
    PER FLOAT,
    WS FLOAT,
    Recent_Salary FLOAT,
    Salary_Year INTEGER,
    Salary_Team TEXT);

\copy nba_all_career from '/docker-entrypoint-initdb.d/nba_all_career.csv' with DELIMITER ',' CSV HEADER;


CREATE TABLE ncaa (
    Player TEXT,
    Position TEXT,
    Height_inches FLOAT,
    Weight_lbs FLOAT,
    College TEXT,
    Draft_Year INTEGER,
    Years_in_college INTEGER,
    G FLOAT,
    MP_per_G FLOAT,
    PTS_per_G FLOAT,
    TRB_per_G FLOAT,
    AST_per_G FLOAT,
    STL_per_G FLOAT,
    BLK_per_G FLOAT,
    TOV_per_G FLOAT,
    FG_Perc FLOAT,
    Three_Perc FLOAT,
    FT_Perc FLOAT,
    EFG_Perc FLOAT,
    PER FLOAT,
    WS FLOAT);

\copy ncaa from '/docker-entrypoint-initdb.d/ncaa.csv' with DELIMITER ',' CSV HEADER;
