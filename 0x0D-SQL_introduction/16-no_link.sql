-- lLsts all records with a name value in the table second_table

SELECT score, name
FROM second_table
WHERE NOT name
ORDER BY score DESC;
