SET @HOUR = -1;
SELECT HOUR_TABLE.HOUR AS HOUR, IFNULL(OUTS.COUNT, 0) AS COUNT
FROM (SELECT (@HOUR := @HOUR + 1) AS HOUR
      FROM ANIMAL_OUTS
      WHERE @HOUR < 23) AS HOUR_TABLE
LEFT JOIN (SELECT HOUR(DATETIME) AS HOUR, (COUNT(HOUR(DATETIME))) AS COUNT
      FROM ANIMAL_OUTS
      GROUP BY HOUR(DATETIME)) AS OUTS
ON OUTS.HOUR = HOUR_TABLE.HOUR

