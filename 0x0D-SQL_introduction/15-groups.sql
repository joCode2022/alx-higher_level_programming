-- lists the number of records with the same score in the table second_table 
-- of the database hbtn_0c_0 in your MySQL server.
-- list should be sorted by the number of records (descending)
-- It displays:
-- The score
-- The number of records for this score with the label number
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY score DESC 
