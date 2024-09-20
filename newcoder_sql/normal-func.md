#### concat function
concat(str1, str2, ...)



#### inert into function
```sql
insert ignore into table (fields split by ',') values (values split by ','),();
```



### replace function
```sql
update titles_test set emp_no=replace(emp_no,10001,10005) where id=5
```

### rename table
```sql
rename table `old_name` to `new_name`
```


### group_concat()
default separator by ','
```sql
select dept_no, group_concat(emp_no) as employees
from dept_emp
group by dept_no
```



### separate pages
```sql
select * from table limit(curPage-1)*pageSize,pageSize;
```


### exists
this function will return True or False
```sql
select *
from employees
where not exists(select emp_no from dept_emp where dept_emp.emp_no=employees.emp_no)
```


### case when
```sql

select e.emp_no, e.first_name, e.last_name, eb.btype, s.salary,
case
    when eb.btype=1 then s.salary*0.1
    when eb.btype=2 then s.salary*0.2
    else s.salary * 0.3
end bonus
from employees e, emp_bonus eb, salaries s
where e.emp_no=eb.emp_no
and e.emp_no=s.emp_no
and s.to_date='9999-01-01'
```


### coalesce(if not null, if is null set a default like 0)
this used in left join or right join with some null value
```sql

select l.date, coalesce(count(user_id),0)
from (select distinct date from login) l left join (select user_id, min(date) as date
      from login
      group by user_id) tmp on l.date=tmp.date
group by date
```

### if function
if(exp1, True result, False result)

```sql

select u.id, u.name, tmp1.grade_sum
from (select user_id, rank() over(order by grade_sum desc) as g_rank, grade_sum
      from (select user_id, sum(if(type='add',1,-1)*grade_num) as grade_sum
            from grade_info
            group by user_id) tmp) tmp1, `user` u
where tmp1.user_id=u.id
and tmp1.g_rank=1

```
