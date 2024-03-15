-- Create lists of all cities of California
SELECT * FROM CITIES
WHERE state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY id ASC;
