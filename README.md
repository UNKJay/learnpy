# learnpy
the process of learning python in one week
1.布尔值和布尔代数的表示完全一致，一个布尔值只有True、False两种值，要么是True，要么是False，在Python中，可以直接用True、False表示布尔值（请注意大小写），也可以通过布尔运算计算出来：and or not
2.空值是Python里一个特殊的值，用None表示。None不能理解为0，因为0是有意义的，而None是一个特殊的空值。此外，Python还提供了列表、字典等多种数据类型，还允许创建自定义数据类型。
3.用全部大写的变量名表示常量只是一个习惯上的用法
4./除法计算结果是浮点数，即使是两个整数恰好整除，结果也是浮点数; 还有一种除法是//，称为地板除，两个整数的除法仍然是整数 ; % 求余
————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
5.list:定义　classmates = ['Michael', 'Bob', 'Tracy']
  用len()函数可以获得list元素的个数;  还可以用-1做索引，直接获取最后一个元素
  用append()可以往list中追加元素到末尾：classmates.append('Adam')
  用insert()可以把元素插入到指定的位置，比如索引号为1的位置：classmates.insert(1, 'Jack')
  删除list末尾的元素，用pop()方法：classmates.pop(); 要删除指定位置的元素，用pop(i)方法
  list里面的元素的数据类型也可以不同,也可以是另一个list

——————————————————————————————————————————————————————————————————————————————————————————
6.tuple:另一种有序列表叫元组：tuple，但是tuple一旦初始化就不能修改。因为tuple不可变，所以代码更安全，如果可能，能用tuple代替list就尽量用tuple。
要定义一个空的tuple，可以写成()：   t=()
要定义一个只有1个元素的tuple，如果你这么定义：t=(1,)　　　　否则会被解释成括号运算符
tuple所谓的“不变”是说，tuple的每个元素，指向永远不变！

——————————————————————————————————————————————————————————————————————————————————————————
7.条件判断:if   x   :                                       (只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False)
             .....
          elif     :
             ....
          else:

——————————————————————————————————————————————————————————————————————————————————————————
8.input(): birth = input('birth: ')
input()返回的数据类型是str，str不能直接和整数比较，必须先把str转换成整数。Python提供了int()函数来完成这件事情:s=int(birth)

——————————————————————————————————————————————————————————————————————————————————————————
9.循环：for x in ...:循环就是把每个元素代入变量x，然后执行缩进块的语句。例如：
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
Python提供一个range()函数，可以生成一个整数序列，再通过list()函数可以转换为list。比如range(5)生成的序列是从0开始小于5的整数
while 循环：while ...:
break和continue的用法和以前一样，不详述。

——————————————————————————————————————————————————————————————————————————————————————————
10.dict & set:
Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。
由于一个key只能对应一个value，所以，多次对一个key放入value，后面的值会把前面的值冲掉：
要避免key不存在的错误，有两种办法，一是通过in判断key是否存在：

>>> 'Thomas' in d
二是通过dict提供的get()方法，如果key不存在，可以返回None，或者自己指定的value：
>>> d.get('Thomas')
>>> d.get('Thomas', -1)
-1
要删除一个key，用pop(key)方法，对应的value也会从dict中删除：
>>> d.pop('Bob')
75
需要牢记的第一条就是dict的key必须是不可变对象!!!!!!

set:set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
要创建一个set，需要提供一个list作为输入集合：
>>> s = set([1, 2, 3])
>>> s
{1, 2, 3}

重复元素在set中自动被过滤：






