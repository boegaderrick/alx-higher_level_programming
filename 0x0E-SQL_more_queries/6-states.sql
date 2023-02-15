-- This script creates a database and a table with non null values.
-- If any of te two already exist the script won't do anything in that particular case

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(256) NOT NULL);
