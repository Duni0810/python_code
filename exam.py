
#coding=utf-8
#Str, 请反转字符串


testname = "hello world"

print testname[::-1]

print testname[::-2]

#给定一个字符串aStr，返回使用空格或者'\t'分割后的倒数第二个子串

teststr = "young\t is \n god\t"

print teststr.split()


#一个学校，有3个办公室，现在有8位老师等待工位的分配，请编写程序，完成随机的分配

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


