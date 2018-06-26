-- This script will create the MySQL server user user_0d_1 w/ all privileges
-- user password will be set to user_0d_1_pwd
-- script shouldn't fail if user already exists
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL ON *.* TO 'user_0d_1'@'localhost';
