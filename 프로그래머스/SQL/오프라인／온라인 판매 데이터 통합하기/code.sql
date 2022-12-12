SELECT DATE_FORMAT(UNION_TABLE.SALES_DATE, '%Y-%m-%d') AS SALES_DATE, 
       UNION_TABLE.PRODUCT_ID,
       UNION_TABLE.USER_ID,
       UNION_TABLE.SALES_AMOUNT
FROM
    (SELECT SALES_DATE, PRODUCT_ID, USER_ID, SALES_AMOUNT
     FROM ONLINE_SALE
     WHERE DATE_FORMAT(SALES_DATE, '%Y-%m') = '2022-03'
     UNION ALL
     SELECT SALES_DATE, PRODUCT_ID, NULL AS USER_ID, SALES_AMOUNT
     FROM OFFLINE_SALE
     WHERE DATE_FORMAT(SALES_DATE, '%Y-%m') = '2022-03') UNION_TABLE
ORDER BY SALES_DATE ASC, PRODUCT_ID ASC, USER_ID ASC
