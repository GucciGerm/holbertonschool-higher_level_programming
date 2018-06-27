-- This script will list all cities contained in the hbtn_0d_usa database
-- Each record will display cities.id, cities.name, states.name
-- Results will be sorted in ascending order by cities.id
SELECT cities.id, cities.name, states.name FROM cities, states
WHERE cities.state_id = states.id;
