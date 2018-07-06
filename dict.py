#coding= utf-8


#字典的使用
##字典的作用是能够直接定位到数据，不用list那样索引下标

info = {'name':'young','id':'100054','sex':'m','add':'china'}

print info['name']
print info['add']

#在我们不确定字典中是否存在某个键而又想获取其值时，可以使用get方法，还可以设置默认值：

age = info.get('age')
print age			# 不存在所以为none

age = info.get('age', 23) #若info中不存在‘age'这个键，则返回默认18
print age


print '===========字典的增删改查============='
print '====改==='
newid = raw_input('输入id ： ')
info['id'] = int(newid)
print '修改之后的id 为 %d '%info['id']

print '===增==='
#如果在使用 变量名['键'] = 数据 时，这个“键”在字典中，不存在，那么就会新增这个元素
newage = raw_input('输入年龄')
info['age'] = int(newage)
print 'age = %d'%info['age']


print '===删==='
print "删除前，%s"%info
del info['age']
print '删除后，%s'%info
# 如果 这么写   del info 就是删除字典 就无法访问了

print '=====清空字典====='
info.clear()
print '清空后字典为%s'%info

print "===字典常见操作======"
info = {'name':'young','id':'100054','sex':'m','add':'china'}

#测量字典中，键值对的个数
print "len(info)",len(info)

#返回一个包含字典所有KEY的列表
print "info.key()",info.keys()

#返回一个字典包含的所有值
print "info.values",info.values()

#返回一个包含所有（键，值）元祖的列表
print "info.items",info.items()

#如果字典中包含key，返回True,否则False
print "是否有key(name)",info.has_key('name')


