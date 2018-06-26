-- This script will list all records of second_table of hbtn_0c_0 database
-- within MySQL server
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
