# Write your MySQL query statement below
SELECT CASE 
  WHEN COUNT(Salary) >= 1 THEN (
    SELECT DISTINCT Salary 
    FROM Employee
    ORDER BY Salary DESC 
    LIMIT 1, 1) 
  ELSE NULL
  END AS SecondHighestSalary
FROM Employee;
