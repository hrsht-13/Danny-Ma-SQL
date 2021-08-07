/* --------------------
   Case Study Questions
   --------------------*/

-- 1. What is the total amount each customer spent at the restaurant?
-- 2. How many days has each customer visited the restaurant?
-- 3. What was the first item from the menu purchased by each customer?
-- 4. What is the most purchased item on the menu and how many times was it purchased by all customers?
-- 5. Which item was the most popular for each customer?
-- 6. Which item was purchased first by the customer after they became a member?
-- 7. Which item was purchased just before the customer became a member?
-- 8. What is the total items and amount spent for each member before they became a member?
-- 9.  If each $1 spent equates to 10 points and sushi has a 2x points multiplier - how many points would each customer have?
-- 10. In the first week after a customer joins the program (including their join date) they earn 2x points on all items, not just sushi - how many points do customer A and B have at the end of January?


--1
-- select s.customer_id,sum(m.price) as amount
-- from dannys_diner.menu m , dannys_diner.sales s 
-- where m.product_id=s.product_id
-- group by s.customer_id
-- order by amount desc

--2
-- select customer_id, count(distinct(order_date))
-- from dannys_diner.sales 
-- group by customer_id

--3
-- select T.customer_id,T.product_name
-- from (select s,customer_id,m.product_name, RANK() over(partition by s.customer_id order by s.order_date) as rank
-- from dannys_diner.sales s , dannys_diner.menu m
-- where s.product_id=m.product_id) T

-- where T.rank=1;

--4
-- select *
-- from (select m.product_name,count(s.product_id) as cnt
-- from dannys_diner.menu m , dannys_diner.sales s 
-- where s.product_id=m.product_id
-- group by m.product_name
-- order by cnt desc) T
--limit 1;

--5
-- select T.customer_id,m.product_name
-- from (select customer_id,product_id,count(product_id) as cnt,RANK() over(partition by customer_id order by count(product_id) desc) as rank
-- from dannys_diner.sales
-- group by customer_id,product_id) T, dannys_diner.menu m
-- where m.product_id=T.product_id and T.rank=1;

--6
-- select T.customer_id,me.product_name
-- from (select s.customer_id, s.order_date, s.product_id,m.join_date,Rank() over(partition by s.customer_id order by s.order_date) as rnk
-- from dannys_diner.sales s , dannys_diner.members m 
-- where s.customer_id=m.customer_id and join_date<=s.order_date ) T, dannys_diner.menu me
-- where T.product_id=me.product_id and T.rnk=1;

--7
-- select T.customer_id,m.product_name
-- from (select s.product_id,s.customer_id, s.order_date,mem.join_date,Rank() over(partition by s.customer_id order by s.order_date desc) as rnk
-- from dannys_diner.sales s , dannys_diner.members mem
-- where s.customer_id=mem.customer_id and s.order_date<mem.join_date) T, dannys_diner.menu m
-- where T.product_id=m.product_id and rnk=1;

--8
-- select T.customer_id,count(T.customer_id),sum(T.price)
-- from(select s.product_id,s.customer_id, s.order_date,mem.join_date, m.price
-- from dannys_diner.sales s , dannys_diner.members mem, dannys_diner.menu m
-- where s.customer_id=mem.customer_id and s.product_id=m.product_id and s.order_date<mem.join_date) T
--group by T.customer_id

--9
-- select T.customer_id,sum(T.pt)
-- from (Select * ,
-- Case
-- when m.product_name='sushi' then 2*(m.price*10)
-- else m.price*10
-- end as PT
-- from dannys_diner.menu m ,dannys_diner.sales s 
-- where s.product_id=m.product_id) T
-- group by T.customer_id

--10
-- select T.customer_id, sum(T.pt)
-- from(select s.customer_id ,
-- Case 
-- when s.order_date<mem.join_date+7 and s.order_date>=mem.join_date  then 20*m.price
-- else m.price*10
-- end as pt
-- from dannys_diner.menu m ,dannys_diner.sales s ,dannys_diner.members mem
-- where s.product_id=m.product_id and s.customer_id=mem.customer_id and s.order_date<'2021-02-01') T
-- group by T.customer_id

--extra 1
-- select s.customer_id,s.order_date,m.product_name,m.price,
-- case
-- when s.order_date>=mem.join_date then 'Y'
-- else 'N'
-- end as member
-- from dannys_diner.menu m ,dannys_diner.sales s left join dannys_diner.members mem on s.customer_id=mem.customer_id
-- where m.product_id=s.product_id 

--extra 2 
-- select * ,
-- case 
-- when T.member='Y' then rank() over(partition by T.customer_id,T.member order by T.order_date)
-- else NULL
-- end as rank
-- from (select s.customer_id,s.order_date,m.product_name,m.price,
-- case
-- when s.order_date>=mem.join_date then 'Y'
-- else 'N'
-- end as member  
-- from dannys_diner.menu m ,dannys_diner.sales s left join dannys_diner.members mem on s.customer_id=mem.customer_id
-- where m.product_id=s.product_id ) T
