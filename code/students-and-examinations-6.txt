# Write your MySQL query statement below
with cte as (
    select * from Students JOIN Subjects
), 

cte_2 as (
    select student_id, subject_name, 
    count(*) as "attended_exams"
    from Examinations 
    group by student_id, subject_name
), 

cte_3 as (
    select c.student_id, c.student_name, c.subject_name, 
    case when c2.attended_exams is not null then c2.attended_exams else 0 end as "attended_exams"
    from cte c LEFT JOIN cte_2 c2 ON 
    c.student_id = c2.student_id and c.subject_name = c2.subject_name
    order by student_id, subject_name
)

select * from cte_3

