### sum window function
1. accumulate values
next one=current+previous
```sql
select emp_no, salary, sum(salary) over(order by emp_no ) as running_total
from salaries 
where to_date='9999-01-01'
```

2. accumulate value partition by some columns
```sql
select u.name as u_n, tmp.date as date, sum(tmp.ps_num) over(partition by u.name order by date) as ps_num
from (select pn.user_id as user_id, pn.date as date, pn.number as ps_num
      from login l, passing_number pn
      where l.user_id=pn.user_id
      and l.date=pn.date) tmp, user u 
where tmp.user_id=u.id
order by date, u_n
```