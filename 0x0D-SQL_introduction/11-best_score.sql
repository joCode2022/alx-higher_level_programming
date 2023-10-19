-- Lists all records with a score >= 10 in second_table of db hbtn_0c_0
-- Results should be in Descending order
-- Both score and names should be displayed
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
