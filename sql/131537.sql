-- 오프라인/온라인 판매 데이터 통합하기

SELECT LEFT(SALES_DATE, 10) AS SALES_DATE, PRODUCT_ID, USER_ID, SALES_AMOUNT
FROM ONLINE_SALE
WHERE SALES_DATE LIKE "2022-03%"
UNION
SELECT LEFT(SALES_DATE, 10) AS SALES_DATE, PRODUCT_ID, NULL AS USER_ID, SALES_AMOUNT
FROM OFFLINE_SALE
WHERE SALES_DATE LIKE "2022-03%"
ORDER BY SALES_DATE, PRODUCT_ID, USER_ID;