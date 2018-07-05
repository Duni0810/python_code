# coding=utf-8
# 列表的 增、删、改、查 的使用


######################增############################
print '======use for ======'
# use  for
namelist = ['young','xiaoming','xiaohua']
for name in namelist :
	print(name)

#use while
print ''
print ''
print '======use while====== '
strlen = len(namelist)
i = 0
while i < strlen :
	print namelist[i]
	i += 1


# 列表的增加文件		append

print '---------列表namelist数据----------'
for name in namelist :
	print name

temp = raw_input('输入名字')
namelist.append(temp)

print '---------列表namelist数据----------'
for name in namelist :
	print name


#通过 extend 将集合逐个加入列表
a = [1,2]
b = [3,4]
a.append(b)
print 'append a',a

a.extend(b)
print 'extend a',a

#insert在指定位置index前插入元素object
a = [0,1,2]
a.insert(1,3)
print '用insert',a

########################改###########################

print("-----修改之前，列表A的数据-----")
for tempName in namelist:
	print(tempName)

#修改元素
namelist[1] = 'xiaoLu'

print("-----修改之后，列表A的数据-----")
for tempName in namelist:
	print(tempName)

########################查#########################
#in, not in, index, count
#in（存在）,如果存在那么结果为true，否则为false
#not in（不存在），如果不存在那么结果为true，否则false

findName = raw_input('请输入要查找的姓名:')

if findName in namelist:
	print('在字典中找到了相同的名字')
else:
	print('没有找到')

#in的方法只要会用了，那么not in也是同样的用法，只不过not in判断的是不存在
#index和count与字符串中的用法相同

a = ['a','b','c','a','b']
#a.index('a', 1, 3) # 注意是左闭右开区间
a.index('a', 1, 4)

print a.count('a')
print a.count('d')

#######################删########################
#del：根据下标进行删除
#pop：删除最后一个元素
#remove：根据元素的值进行删除

movieName = ['加勒比海盗','骇客帝国','第一滴血','指环王','霍比特人','速度与激情']
print('------删除之前------')
for tempName in movieName:
        print(tempName)

del movieName[2]

print('------删除之后------')
for tempName in movieName:
        print(tempName)
###########################################

movieName.pop()

print('------删除之后------')
for tempName in movieName:
    print(tempName)
###########################################

movieName.remove('指环王')

print('------删除之后------')
for tempName in movieName:
    print(tempName)
###########################################

#######################排序#######################
# reverse，sort  没有返回值

a = [1, 4, 2, 3]
print a
print 'use reverse'
a.reverse()
print a
print 'use sort'
a.sort()
print a
print 'use sort(reverse)'
a.sort(reverse=True)
print a

