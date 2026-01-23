-- List all cities of California
SELECT id, name
FROM states
WHERE name = 'California'
ORDER BY states.id ASC;
