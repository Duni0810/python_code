
#coding=utf-8
#Str, 请反转字符串

print '='*5,'one title start','='*5

testname = "hello world"
print testname[::-1]

print '='*5,'one title end  ','='*5
print ''
#给定一个字符串aStr，返回使用空格或者'\t'分割后的倒数第二个子串
print '='*5,'two title start','='*5
teststr = "young\t is \n god\t"
print teststr.split()
print '='*5,'two title end  ','='*5
print ''

#一个学校，有3个办公室，现在有8位老师等待工位的分配，请编写程序，完成随机的分配
print '='*5,'three title start','='*5

import random

#定义一个列表用来保存3个办公室
offices = [[], [], []]
#定义一个列表用来保存8个老师
names = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

for name in names :
	index = random.randint(0, 2)
	offices[index].append(name)
i = 1
for tempName in offices :
	print '办公室%d有%d个人'%(i, len(tempName))
	i += 1

	for name in tempName :
		print '%s'%name,
	print ''
	print '-'*20
print '='*5,'three title end  ','='*5
print ""


#1. 编程实现对一个元素全为数字的列表，求最大值、最小值
print '='*5,'four title start','='*5
mylist  = [123, 447, 323, 1235, 675, 21, 12]
print 'max(mylist)',max(mylist)
print 'min(mylist)',min(mylist)
print '='*5,'four title end  ','='*5
print ""

#2. 编写程序，完成以下要求：

#统计字符串中，各个字符的个数
#比如："hello world" 字符串统计的结果为： h:1 e:1 l:3 o:2 d:1 r:1 w:1

print '='*5,'five title start','='*5
mystr = 'hello world'
charnum = {}

for char in mystr :
	charnum[char] = mystr.count(char)
	#print 'charnum',charnum.keys()
	#print charnum[char]
#print charnum['l']  		#	会自动索引'l'的数据	
print ''
print charnum

print '='*5,'four title end  ','='*5
print ""

'''
4. 编写程序，完成“名片管理器”项目

需要完成的基本功能：
添加名片
删除名片
修改名片
查询名片
退出系统
程序运行后，除非选择退出系统，否则重复执行功能
'''
print '='*5,'six title start','='*5
mylist = [{'name':'young' ,'id':'100054'},{'name':'qq','id':'1234'}]


while True :
	print '1.添加名片'
	print '2.删除名片'
	print '3.修改名片'
	print '4.查询名片'
	print '5.退出系统(或者回车)'
	mselect = raw_input("输入你的选择：")
	select = int(mselect)

	#添加名字
	if select == 1 :
		newdict = {'name':'','id':''}
		#newname = raw_input('输入名字:')
		newdict['name'] = raw_input('输入名字:')
		newdict['id'] = raw_input('输入id:')
		#newid = raw_input('输入id:')
		mylist.append(newdict)
		print ''

	#删除名片
	elif select == 2 :
		i = 0
		while i < len(mylist) :
			print i
			print 'name:',mylist[i]['name']
			print ' id :',mylist[i]['id']
			print ""
			i += 1 
		print '查询完毕'
		tempnum = raw_input('要删除几号：')
		del mylist[int(tempnum)]
		print 'delete success'
		print ''


	#修改名片
	elif select == 3 :
		i = 0
		while i < len(mylist) :
			print i
			print 'name:',mylist[i]['name']
			print ' id :',mylist[i]['id']
			print ""
			i += 1 
		print '查询完毕'
		tempnum = raw_input('要修改几号：')
		mylist[int(tempnum)]['name'] = raw_input('要修改的name:')
		mylist[int(tempnum)]['id']   = raw_input('要修改的id') 
		print 'modified success'

	#查询名片
	elif select == 4 :
		#打印 列表
		i = 0
		while i < len(mylist) :
			print 'name:',mylist[i]['name']
			print ' id :',mylist[i]['id']
			print ""
			i += 1 
		print '查询完毕'


	elif select == 5 : 
		print 'thank you'
		break
	
	else :
		pass

print '='*5,'six title end  ','='*5
print ""
