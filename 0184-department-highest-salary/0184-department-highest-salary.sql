select D.name as Department,E.name as Employee, E.salary as Salary from Department as D  join Employee as E on D.id = E.departmentid where (E.departmentId,E.salary) in (SELECT departmentId, MAX(salary)
FROM Employee
GROUP BY departmentId);