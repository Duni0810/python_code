#coding=utf-8
#
#
#创建对象后，python解释器默认调用__init__()方法；
#当删除一个对象时，python解释器也会默认调用一个方法，这个方法为__del__()方法


import time

class animal(object) :

	#初始化方法，创建对象后会自动被调用
	
	def __init__(self, name) :
		print '__init__方法被调用'
		self.__name = name

	#析构方法，当对象被删除时候，会自动被调用

	def __del__(self) :
		print '__del__方法被调用'
		print '%s对象被删除……'%self.__name

dog = animal('小花狗')

#当有1个变量保存了对象的引用时，此对象的引用计数就会加1
#当使用del删除变量指向的对象时，如果对象的引用计数不是1，
#比如3，那么此时只会让这个引用计数减1，即变为2，当再次调用del时，
#变为1，如果再调用1次del，此时会真的把对象进行删除
#
#所以得一个一个的删引用在del
dog1 = dog 

#删除对象引用
del dog1
#删除对象
del dog

print '还有2s后结束'
time.sleep(2)


print '='*40







