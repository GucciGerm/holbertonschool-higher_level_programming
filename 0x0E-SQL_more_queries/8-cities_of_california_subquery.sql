-- This script will list all the cities of California that can be found in
-- the database hbtn_0d_usa
-- The states table contains only 1 record where name = California
-- Results must be in ascending order by cities.id
SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states
WHERE name = California);
