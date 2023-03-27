group_concat主要是用于拼接select语句，特别是在动态取值的时候， 
例如case when和sum if的时候。

但由于group_concat的默认配置长度有限，所以在处理大量数据的时候会发现一些内容被截取了
其实MYSQL内部对这个是有设置的，不设置的话，默认是1024，如果我们需要更大，就需要手工修改。

如果找不到配置文件的话可以看这个[MYSQL文件配置](MYSQL配置文件地址.md)

大家可以设置自己想要的值，我这边举例设置的102400

在MYSQL配置文件中加上这个: 
```shell
group_concat_max_len = 102400
```
或者也可以在电脑上执行以下命令:
```shell
SET GLOBAL group_concat_max_len=102400;
SET SESSION group_concat_max_len=102400;
```



