


#### add primary key
```sql
ALTER TABLE tbl_name ADD PRIMARY KEY (col_list);
// add primary key, index must be unique, not null 
```


#### add unique index 
```sql
ALTER TABLE tbl_name ADD UNIQUE index_name (col_list);
// index value must be unique
```


#### add normal index
```sql
ALTER TABLE tbl_name ADD INDEX index_name (col_list);
// add normal index, index value can be shown mutiple times
```


#### add fulltext index
```sql
ALTER TABLE tbl_name ADD FULLTEXT index_name (col_list);
// fulltext index
```


#### delete index
```sql
DROP INDEX index_name ON tbl_name;
// or
ALTER TABLE tbl_name DROP INDEX index_name;
ALTER TABLE tbl_name DROP PRIMARY KEY;
```


#### use index
```sql
select *
from salaries
force index (idx_emp_no)
where emp_no=10005
```
