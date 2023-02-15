-- This script creates a use and grants them full access

CREATE USER IF NOT EXISTS'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* to user_0d_1@localhost;
