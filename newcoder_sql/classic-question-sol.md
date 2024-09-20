

### about the mid number
1. 用一条规则统一奇数个数时和偶数个数时的中位数位置。无论奇偶，中位数的位置距离（个数+1）/2 小于1
eg: 
```sql
select id,job,score,s_rank
from 
(select *
        ,(row_number()over(partition by job order by score desc))as s_rank
	    ,(count(score)over(partition by job))as num
        from grade)t1
where abs(t1.s_rank-(t1.num+1)/2)<1
order by id;
```



### about the mi
1. 当某一数的正序和逆序累计均大于整个序列的数字个数的一半即为中位数
https://www.nowcoder.com/practice/165d88474d434597bcd2af8bf72b24f1?tpId=82&rp=1&ru=%2Factivity%2Foj&qru=%2Fta%2Fsql%2Fquestion-ranking <br>
比如:<br>
A A B B C C D D<br> 
1 2 3  4  5 6  7 8<br>
8 7 6  5  4  3 2 1<br>
那么上面的4，5以及5，4就是中位数，如果是奇数的话，就只有1个<br>
再比如<br>
A2个，B3个，C5个，D2个，<br>
正序2，5，10，12<br>
倒序12，10，7，2<br>
正序和12，大于等于6的，为C,D，<br>
逆序和为12，大于等于6的为ABC，所以最后中位数为C<br>
```sql
select grade
from (select grade, (select sum(number) from class_grade) as total_number,
      sum(number) over(order by grade) as up, sum(number) over(order by grade desc) as down
      from class_grade) tmp1
where up>=total_number/2 and down>=total_number/2
order by grade
```

