一般情况下，my.cnf 在 /etc/my.cnf 或 /etc/mysql/my.cnf 目录下

有时候可能会用不同的方式来安装MYSQL，例如homebrew 

这个时候我们可以用下面这个命令来查看配置文件引用的路径
```shell
mysqld --help --verbose | more
```

通过这命令，可以看出mysql默认调用的配置文件路径：

Default options are read from the following files in the given order:
/etc/my.cnf /etc/mysql/my.cnf /opt/homebrew/etc/my.cnf ~/.my.cnf

这个时候我们可以去这三个目录分别看一下，然后在目录中配置