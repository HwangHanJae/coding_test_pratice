SELECT FOOD_TYPE, REST_ID, REST_NAME, FAVORITES
FROM REST_INFO R
JOIN
    (SELECT MAX(FAVORITES) AS MAX_FAVOR FROM REST_INFO GROUP BY FOOD_TYPE) AS I 
    ON R.FAVORITES = I.MAX_FAVOR 
GROUP BY FOOD_TYPE
ORDER BY FOOD_TYPE DESC