LOAD DATA LOCAL INFILE '/Users/tds/Desktop/SOU/worldCup_database/WorldCup/data/raw/nations.csv'
INTO TABLE Nation
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(nation_name, confederation, fifa_ranking, group_letter);
