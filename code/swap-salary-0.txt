/* Write your T-SQL query statement below */
UPDATE Salary
SET sex = CASE sex
        WHEN 'm' THEN 'f'
        WHEN 'f' THEN 'm'
        END;
