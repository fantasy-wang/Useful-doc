#### add foreign key
```sql
gramma: alter table table_name add constraint FK_ID foreign key(table_column_name) REFERENCES external_table_name(external_table_column_name);

eg: alter table audit add constraint emp_no foreign key(emp_no) references employees_test(id);
```