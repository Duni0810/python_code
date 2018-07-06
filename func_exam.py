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

myprime(100, 200)