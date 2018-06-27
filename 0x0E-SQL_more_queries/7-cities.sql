-- This script will create a database hbtn_0d_usa and create table cities
-- within the hbtn_0d_usa, id must be a unique integer, auto generated value
-- and primary key, state_id must be an integer can't be null and is the
-- foreign key that references the id of the states table, name varchar can't
-- be empty
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (id INT AUTO_INCREMENT PRIMARY_KEY NOT NULL,
state_id INT NOT NULL, FOREIGN KEY (state_id) REFERENCES states(id),
name VARCHAR(256) NOT NULL);
