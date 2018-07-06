#coding=utf-8

# 这个主要讲解下lambda用法
stus = [
    {"name":"zhangsan", "age":18}, 
    {"name":"lisi", "age":19}, 
    {"name":"wangwu", "age":17}
]

stus.sort(key = lambda x:x['name'])
print '按照name排序',stus

stus.sort(key = lambda x:x['age'])
print '按照 age 排序',stus