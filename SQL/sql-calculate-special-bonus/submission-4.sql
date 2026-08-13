-- Write your query below
SELECT employee_id, 
    CASE
    WHEN employee_id %2 != 0 AND name not like 'M%' then salary
    ELSE 0
    END AS bonus
FROM employees
ORDER BY employee_id;