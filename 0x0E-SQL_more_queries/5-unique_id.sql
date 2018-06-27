-- This script will create a table unique_id on MySQL server
-- will have an id integer with a default value of 1 also unique
CREATE TABLE IF NOT EXISTS unique_id(int INT DEFAULT 1 UNIQUE,
name VARCHAR(256));
