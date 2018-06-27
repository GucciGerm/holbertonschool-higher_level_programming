-- This script will create a database hbtn_0d_usa and a states table
-- id input should be unique, auto-generated, primary key and not null
-- If the database hbtn_0d_usa and states table both individually exist
-- the script should not fail
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (id INT UNIQUE AUTO_INCREMENT PRIMARY KEY NOT
NULL, name VARCHAR(256) NOT NULL);
