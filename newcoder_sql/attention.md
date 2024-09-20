##### Sql script Attention



1. sql use subset need to remember that subset need to create a name and then use
```sql
    select * from (
                      select date, rank() over(order by `clumon` desc / asc) as `ranking`
                      from `table`
                  ) tmp where ranking = 3

```

2.