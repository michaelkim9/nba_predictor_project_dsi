FROM postgres

COPY initdb.sql /docker-entrypoint-initdb.d/initdb.sql
COPY data/nba_draft.csv /docker-entrypoint-initdb.d/nba_draft.csv
COPY data/team_salary.csv /docker-entrypoint-initdb.d/team_salary.csv
COPY data/salary_cap.csv /docker-entrypoint-initdb.d/salary_cap.csv
COPY data/nba_2016.csv /docker-entrypoint-initdb.d/nba_2016.csv
COPY data/nba_all_career.csv /docker-entrypoint-initdb.d/nba_all_career.csv
COPY data/ncaa.csv /docker-entrypoint-initdb.d/ncaa.csv