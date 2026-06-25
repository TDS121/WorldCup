-- use usr_skerrittt_1;

-- Nations
INSERT INTO Nation (nation_name, confederation, fifa_ranking, group_letter) VALUES
('Brazil', 'CONMEBOL', 1, 'A'),
('France', 'UEFA', 2, 'B'),
('England', 'UEFA', 3, 'C'),
('Argentina', 'CONMEBOL', 4, 'D');

-- Stadiums
INSERT INTO Stadium (stadium_name, city, country, capacity) VALUES
('MetLife Stadium', 'New York', 'USA', 82500),
('AT&T Stadium', 'Dallas', 'USA', 80000);

-- Players
INSERT INTO Player (first_name, last_name, nation_id, position, kit_number, date_of_birth) VALUES
('Vinicius', 'Jr', 1, 'FW', 7, '2000-07-12'),
('Kylian', 'Mbappe', 2, 'FW', 10, '1998-12-20'),
('Jude', 'Bellingham', 3, 'MF', 8, '2003-06-29'),
('Lionel', 'Messi', 4, 'FW', 10, '1987-06-24');

-- Games
INSERT INTO Game (stadium_id, home_id, away_id, game_date, tournament_stage, home_score, away_score, attendance) VALUES
(1, 1, 2, '2026-06-15', 'Group Stage', 2, 1, 80000),
(2, 3, 4, '2026-06-16', 'Group Stage', 1, 1, 78000);

-- Player_Game
INSERT INTO Player_Game (game_id, player_id, minutes_played, yellow_cards, red_cards, is_starter) VALUES
(1, 1, 90, 0, 0, TRUE),
(1, 2, 90, 1, 0, TRUE),
(2, 3, 90, 0, 0, TRUE),
(2, 4, 85, 0, 0, TRUE);

-- Goals
INSERT INTO Goal (player_id, game_id, goal_minute, is_own_goal) VALUES
(1, 1, 23, FALSE),
(1, 1, 67, FALSE),
(2, 1, 45, FALSE),
(3, 2, 10, FALSE),
(4, 2, 78, FALSE);

SELECT * FROM Stadium;