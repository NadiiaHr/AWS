WITH table1 AS 
    (SELECT DISTINCT name,
         high,
         ts,
         SUBSTRING(ts,
         12,
         2) AS day_hour
    FROM bucket_project3), table2 AS 
    (SELECT table1.name AS company_name,
         MAX(table1.high) AS high_price_hour,
         table1.day_hour AS hour_of_day
    FROM table1
    GROUP BY  table1.name, table1.day_hour)
SELECT table2.company_name,
         table2.high_price_hour,
         table2.hour_of_day,
         table1.ts
FROM table1, table2
WHERE table1.name = table2.company_name
        AND table1.high = table2.high_price_hour
        AND table1.day_hour = table2.hour_of_day
ORDER BY  table2.company_name, table2.hour_of_day
