-- 서울에 위치한 식당 목록 출력하기

SELECT B.REST_ID, B.REST_NAME, B.FOOD_TYPE, B.FAVORITES, B.ADDRESS, A.SCORE
FROM (
    SELECT REST_ID, ROUND(AVG(REVIEW_SCORE), 2) AS SCORE
    FROM REST_REVIEW
    GROUP BY REST_ID
) AS A
JOIN REST_INFO AS B
ON A.REST_ID=B.REST_ID
WHERE B.ADDRESS LIKE "서울%"
ORDER BY A.SCORE DESC, B.FAVORITES DESC;