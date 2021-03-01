```sql
SELECT buyer_id,buy_date, book_name,price
FROM orderInfo A
LEFT JOIN library B
ON A.book_id = B.book_id
WHERE book_name = 'Looking with Elice'
OR A.buy_date between '2020-07-27' and '2020-07-31'
ORDER BY A.buy_date ASC
;
/*
아래의 2개의 조건 중 하나라도 충족하는 쿼리 값을 구매일 기준으로 오름차순 정렬해야함

1. 책 이름(book_name)이 Looking with Elice인 도서
2. 책 구매일(buy_date)이 2020-07-27부터 2020-07-31까지인 모든 도서

*/
```
