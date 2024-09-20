1. re in python
import re
re.findall('\d+|[a-zA-Z]+', string)   
```python
import re
a = "not 404 found 张三 99 深圳"
list = a.split(" ")
print(list)
res = re.findall('\d+|[a-zA-Z]+', a)
for i in res:
    if i in list:
        list.remove(i)
new_str=" ".join(list)
print(res)
print(new_str)
```