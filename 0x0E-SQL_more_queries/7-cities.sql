-- This script creates a database and a table with non null values.
-- If any of te two already exist the script won't do anything in that particular case

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(256) NOT NULL,
state_id INT NOT NULL, FOREIGN KEY(state_id) REFERENCES states(id));
