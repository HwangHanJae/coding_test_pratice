-- 첫번째 방법
SELECT ID, NAME, HOST_ID
FROM PLACES AS O
JOIN 
    (SELECT HOST_ID AS H_USER , COUNT(HOST_ID) AS CNT
    FROM PLACES
    GROUP BY HOST_ID
    HAVING CNT >= 2) AS U
ON O.HOST_ID = U.H_USER
ORDER BY ID

-- 두번째 방법
SELECT ID, NAME, HOST_ID
FROM PLACES
WHERE HOST_ID
    IN (SELECT HOST_ID FROM PLACES GROUP BY HOST_ID HAVING COUNT(HOST_ID) >= 2)
ORDER BY ID