# Write your MySQL query statement below
select id1 as id, student from
(  
  (select id-1 as id1, student from seat where id%2=0)
  union all
  (select IF(id=(
    select MAX(id) from seat
  ),id,id+1) as id1, student from seat where id%2=1)
) as c order by id