-- 카테고리 별 상품 개수 구하기

SELECT LEFT(PRODUCT_CODE, 2) AS CATEGORY, COUNT(PRODUCT_ID) AS PRODUCTS
FROM PRODUCT
GROUP BY CATEGORY
ORDER BY CATEGORY;