-- --1
-- select count(*)
-- from pizza_runner.customer_orders

-- --2
-- select count(distinct(order_time))
-- from pizza_runner.customer_orders

-- --3
-- Update pizza_runner.runner_orders
-- set cancellation= NULL
-- where cancellation in ('null','');

-- select runner_id,count(*)
-- from pizza_runner.runner_orders
-- where cancellation isnull
-- group by runner_id

-- --4
-- select c.pizza_id,p.pizza_name,count(*)
-- from pizza_runner.runner_orders o,pizza_runner.customer_orders c , pizza_runner.pizza_names p
-- where o.order_id=c.order_id and c.pizza_id=p.pizza_id and o.cancellation isnull
-- group by c.pizza_id, p.pizza_name

-- --5
-- select c.customer_id, p.pizza_name, count(p.pizza_name)
-- from pizza_runner.customer_orders c , pizza_runner.pizza_names p
-- where c.pizza_id=p.pizza_id
-- group by p.pizza_name, c.customer_id
-- order by c.customer_id

-- --6
-- select max(cnt)
-- from(select count(*) as cnt
-- from pizza_runner.runner_orders o,pizza_runner.customer_orders c
-- where o.cancellation isnull and c.order_id=o.order_id
-- group by c.order_time) t

-- --7
