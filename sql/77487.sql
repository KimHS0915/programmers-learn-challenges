-- 헤비 유저가 소유한 장소

SELECT B.ID, B.NAME, B.HOST_ID
FROM (
    SELECT HOST_ID
    FROM PLACES
    GROUP BY HOST_ID
    HAVING COUNT(*) > 1
) AS A
LEFT JOIN PLACES AS B
ON A.HOST_ID=B.HOST_ID
ORDER BY ID;