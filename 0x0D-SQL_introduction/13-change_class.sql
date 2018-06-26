-- This script removes all records with a score <= 5 in the second_table
-- of the hbtn_0c_0 in MySQL server
DELETE FROM second_table WHERE score <= 5 ORDER BY score DESC;
