#coding=utf-8



#遍历 字符串 ，列表，元组，字典等数据结构

#字符串遍历
mystr = "welcome to young world"
for char in mystr :
	print char,' ',

print ''

#列表遍历
mylist = [1, 2, 3, 4, 5]
for num in mylist :
	print num ,
print type(num)
print ''

#元组遍历
myturple = (1, 2, 3, 4, 5)
for num in myturple :
	print num,
print ''
#字典遍历----value（值）
mydict = {'name':'young','id':'100054','sex':'m'}
for value in mydict.values() :
	print value

#字典遍历---key（键）
for key in mydict.keys() :
	print key

#字典遍历---item项（元素）
for item in mydict.items() :
	print item

#字典遍历 key-value (键值对)
for key,value in mydict.items() :
	print 'key = %s ,value = %s'%(key, value)


#实现用带下标索引遍历1

i = 0
for char in mylist :
	print 'i = %d char = %d'%(i, char)
	i += 1

#实现下标索引遍历 2

for j, chr in enumerate(mylist) :
	print j, chr
