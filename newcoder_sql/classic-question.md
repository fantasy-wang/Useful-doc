
### second day login question
```sql

-- first day login
select user_id, min(date)
from login
group by user_id


-- second day 
select user_id, DATE_ADD(min(date),INTERVAL 1 DAY)
from login
group by user_id


-- all users
select count(distinct user_id)
from login


-- result
select round(count(distinct user_id)/(select count(distinct user_id) from login),3)
from login
where (user_id,date)
in (select user_id, DATE_ADD(min(date),INTERVAL 1 DAY)
    from login
    group by user_id)
```