/* 2021-06-03 SQL 강의

MySQL은 뒤에 세미콜론을 붙이지 않아도 동작은 함
하지만 그런식으로 작성하면, 다음 문장을 인식 못하기 때문에 붙임

주석은 #, --, /**\/을 사용함
마지막거는 여러줄 주석
*/

use adventureworks;
-- 지정한 DB 사용


-- SELECT -------------------------------------------------------------------------
select * from salesorderheader;
-- Limit to 1000 rows로 가져오는 레코드 수가 제한되어있으므로
-- 더 많은 데이터를 보고싶다면 제한을 풀어줘야함
-- CDS : citizen data science 

select * from salesorderdetail;


-- JOIN ---------------------------------------------------------------------------------
-- inner join, outer join
-- 두 테이블을 속성을 기준으로 합치는 것

select soh.SalesOrderID, soh.OrderDate, sod.salesOrderid, ProductID, OrderQty
from selaesorderheader soh join salesorderdetail sod
on soh.SalesOrderID = sod.SalesOrderID;

-- inner join : 속성이 양쪽에 존재하는 것에 대해서만 join. 
-- outter join : 데이터가 한쪽에만 있는 경우에도 join됨. 데이터가 없는 부분은 null을 채워넣음
-- join 앞에 outter를 지정해줘야 함. left outer, right outer

-- inner join -----------------------------------
select sod.productid, p.productid, p.name
from salesorderdetail sod join product p
on sod.productid = p.productid;
-- 121317 rows(records)

-- outer join ------------------------------------
-- left outer join
select sod.productid, p.productid, p.name
from salesorderdetail sod left outer join product p
on sod.productid = p.productid;
-- 121317 rows(records)

-- right outer join -----------
select sod.productid, p.productid, p.name
from salesorderdetail sod right outer join product p
on sod.productid = p.productid;
-- 121555 rows(records)

-- null? ----------------------
-- 주문이 이뤄지지 않은 제품의 id를 출력
select sod.productid, p.productid, p.name
from salesorderdetail sod right outer join product p
on sod.productid = p.productid
where sod.productid is null;
-- 238 rows

# 오늘 늦겠다..;;;

