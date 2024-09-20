#### SQL Rank Function

Use Cases:
1. data needs to be ranked
2. this is not continuously <br/>
   eg: 1,2,2,4
3. needs to find the first, second, last two data <br/>
eg: find the last third one <br/>
```sql
    select * from (
                   select date, rank() over(order by `clumon` desc / asc) as `ranking`
                   from `table`
               ) tmp where ranking = 3
```

#### SQL Dense_rank Function

Use Cases:
1. date needs to be ranked
2. data needs to be ranked continuously <br/>
eg: 1,2,2,3 not the 1,2,2,4(rank function)
```sql
select emp_no, salary, dense_rank() over(order by salary desc) as t_rank
from salaries
```

### difference of rank,dense_rank and row_number
1. rank()排序相同时会重复，总数不变，即会出现1、1、3这样的排序结果;
2. dense_rank()排序相同时会重复，总数会减少，即会出现1、1、2这样的排序结果;
3. row_number()排序相同时不会重复，会根据顺序排序.


