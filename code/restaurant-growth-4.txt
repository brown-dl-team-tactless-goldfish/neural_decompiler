select
    distinct customer.visited_on,
    sum(c.amount) amount,
    round(sum(c.amount) / 7, 2) average_amount
from customer
join customer c on
    c.visited_on between date_sub(customer.visited_on, interval 6 day) and customer.visited_on
where customer.visited_on >= date_add(
    (select min(visited_on) from customer),
    interval 6 day
)
group by customer.visited_on, customer.customer_id
order by customer.visited_on