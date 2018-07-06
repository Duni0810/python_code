#coding=utf-8
#

a = [1, 2]
b = a
print b

a.append(3)
print 'a = ',a
print 'b = ',b

#在python中，值是靠引用来传递来的
#我们可以用id()来判断两个变量是否为同一个值的引用。 我们可以将id值理解为那块内存的地址标示。

m = 1
n = m
print 'n = m'
print 'id(m)',id(m)
print 'id(n)',id(n)


