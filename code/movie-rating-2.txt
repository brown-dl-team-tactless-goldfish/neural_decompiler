# Write your MySQL query statement below
with cte as (
    select user_id, 
    count(1) over(partition by user_id) as "user_count"
    from MovieRating 
    
), cte_2 as (
    select *, 
    dense_rank() over(order by user_count desc) as "ranking"
    from cte group by user_id
    
), cte_3 as (
    select u.user_id, u.name, m.ranking
    from cte_2 m INNER JOIN Users u ON u.user_id = m.user_id
    
), cte_4 as (
    select name from cte_3
    where ranking = 1
    order by name limit 1
    
), cte_5 as (
    select movie_id, 
    count(1) over(partition by movie_id) as "movie_count", 
    rating
    from MovieRating 
    where EXTRACT(MONTH from created_at) = 2 and EXTRACT(YEAR from created_at) = 2020
), cte_6 as (

    select *, sum(rating) as "total_rating", 
    count(1) as "total_movies" from cte_5 group by movie_id
    
), cte_7 as (

    select m.movie_id, m.title,
    c.total_rating, c.total_movies, 
    c.total_rating / c.total_movies as "average_rating"
    from 
    Movies m INNER JOIN cte_6 c ON m.movie_id = c.movie_id
    order by average_rating desc, title limit 1
)
select c4.name as "results" from cte_4 c4
UNION 
select c7.title from cte_7 c7

