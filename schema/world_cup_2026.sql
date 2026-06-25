-- use usr_skerrittt_1;

CREATE TABLE Nation (
    nation_id INT AUTO_INCREMENT PRIMARY KEY,
    nation_name VARCHAR(100) NOT NULL,
    confederation VARCHAR(25),
    fifa_ranking INT,
    group_letter CHAR(1)
);

CREATE TABLE Stadium (
    stadium_id INT AUTO_INCREMENT PRIMARY KEY,
    stadium_name VARCHAR(100) NOT NULL,
    city VARCHAR(50),
    country VARCHAR(50),
    capacity INT
);

CREATE TABLE Player (
    player_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    nation_id INT,
    position VARCHAR(20),
    kit_number INT,
    date_of_birth DATE,

    FOREIGN KEY (nation_id) REFERENCES Nation(nation_id)
);

CREATE TABLE Game (
    game_id INT AUTO_INCREMENT PRIMARY KEY,
    stadium_id INT,
    home_id INT,
    away_id INT,
    game_date DATE,
    tournament_stage VARCHAR(35),
    home_score INT,
    away_score INT,
    attendance INT,

    CONSTRAINT fk_stadium FOREIGN KEY (stadium_id) REFERENCES Stadium(stadium_id),
    CONSTRAINT fk_home_id FOREIGN KEY (home_id) REFERENCES Nation(nation_id),
    CONSTRAINT fk_away_id FOREIGN KEY (away_id) REFERENCES Nation(nation_id)
);

CREATE TABLE Player_Game (
    game_id INT,
    player_id INT,
    minutes_played INT,
    yellow_cards INT,
    red_cards INT,
    is_starter BOOLEAN,

    PRIMARY KEY(player_id, game_id),

    FOREIGN KEY (game_id) REFERENCES Game(game_id),
    FOREIGN KEY (player_id) REFERENCES Player(player_id)
);

CREATE TABLE Goal (
    goal_id INT AUTO_INCREMENT PRIMARY KEY,
    player_id INT,
    game_id INT,
    goal_minute INT,
    is_own_goal BOOLEAN,

    FOREIGN KEY (player_id) REFERENCES Player(player_id),
    FOREIGN KEY (game_id) REFERENCES Game(game_id)
);

