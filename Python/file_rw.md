1. open file, write file and file close
```python
file_path = "..."
f = open(file_path, "wb")
try:
    f.write("hello world")
except:
    pass
finally:
    f.close()
```