SELECT DISTINCT(M.CART_ID)
FROM (SELECT CART_ID,NAME FROM CART_PRODUCTS WHERE NAME LIKE '%Milk%') AS M
JOIN (SELECT CART_ID, NAME FROM CART_PRODUCTS WHERE NAME LIKE '%Yogurt%') AS Y
ON M.CART_ID = Y.CART_ID
ORDER BY M.CART_ID