WITH TOP1 AS (
    SELECT BOARD_ID
    FROM USED_GOODS_BOARD
    ORDER BY VIEWS DESC
    LIMIT 1
    
) 

SELECT CONCAT_WS('/','/home/grep/src',FILE.BOARD_ID,
        CONCAT(FILE_ID,
        FILE_NAME,
        FILE_EXT)) AS FILE_PATH
FROM TOP1
JOIN USED_GOODS_FILE AS FILE
ON TOP1.BOARD_ID = FILE.BOARD_ID
ORDER BY FILE_ID DESC