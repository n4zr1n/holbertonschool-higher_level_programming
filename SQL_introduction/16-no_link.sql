-- a script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server.
SELECT score, name
FROM second_table
WHERE name is not null
ORDER BY score DESC;
