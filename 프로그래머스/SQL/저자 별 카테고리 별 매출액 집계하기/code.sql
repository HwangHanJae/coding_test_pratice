SELECT 
    A.AUTHOR_ID AS AUTHOR_ID,
    A.AUTHOR_NAME AS AUTHOR_NAME,
    B.CATEGORY AS CATEGORY,
    SUM(SALES* PRICE) AS TOTAL_SALES
FROM BOOK B
JOIN AUTHOR A
ON B.AUTHOR_ID = A.AUTHOR_ID
JOIN BOOK_SALES S
ON S.BOOK_ID = B.BOOK_ID
WHERE DATE_FORMAT(S.SALES_DATE, '%Y-%m') = '2022-01'
GROUP BY AUTHOR_ID, CATEGORY
ORDER BY AUTHOR_ID ASC, CATEGORY DESC