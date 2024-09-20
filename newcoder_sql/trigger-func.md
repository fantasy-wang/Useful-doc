#### create trigger

```sql
create trigger triggerName 
after/before insert/update/delete on 表名 
for each row #fixed on mysql 
begin 
 sql语句; 
end; 
```