SELECT
    YEAR(SALES_DATE) AS YEAR,
    MONTH(SALES_DATE) AS MONTH,
    U.GENDER AS GENDER,
    COUNT(DISTINCT(U.USER_ID)) AS USERS
FROM USER_INFO U
JOIN ONLINE_SALE O
ON U.USER_ID = O.USER_ID
GROUP BY YEAR(SALES_DATE), MONTH(SALES_DATE), U.GENDER
HAVING GENDER IS NOT NULL
ORDER BY YEAR, MONTH, GENDER