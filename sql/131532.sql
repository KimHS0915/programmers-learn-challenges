-- 년, 월, 성별 별 상품 구매 회원 수 구하기

SELECT YEAR(A.SALES_DATE) AS YEAR, MONTH(A.SALES_DATE) AS MONTH, 
        B.GENDER AS GENDER, COUNT(DISTINCT B.USER_ID) AS USERS
FROM (
    SELECT SALES_DATE, USER_ID
    FROM ONLINE_SALE
    WHERE SALES_DATE LIKE "2022%"
) AS A
JOIN USER_INFO AS B
ON A.USER_ID=B.USER_ID
WHERE B.GENDER IS NOT NULL
GROUP BY YEAR, MONTH, GENDER
ORDER BY YEAR, MONTH, GENDER;