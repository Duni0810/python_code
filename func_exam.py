#coding=utf-8

#2.用函数实现求100-200里面所有的素数
#提示：素数的特征是除了1和其本身能被整除，其它数都不能被整除的数

import math

def myprime(start , end):
	
	print 'start'
	while start < end :

		i = 2
		while i < start:

			if start%i == 0 :
				break
			
			i = i + 1
		if start <= i :
			print start
		start = start + 1

#请用函数实现一个判断用户输入的年份是否是闰年的程序
#1.能被400整除的年份 
#2.能被4整除，但是不能被100整除的年份
#以上2种方法满足一种即为闰年

def myleap(year) :
	if year % 400 == 0 :
		print 'leap year'
		return 1
	elif year % 4 == 0 and year % 100 != 0 :
		print 'leap year'
		return 1
	print 'no leap year'
	return 0



myprime(100, 200)
myleap(2004)
