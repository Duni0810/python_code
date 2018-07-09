#coding=utf-8
#
#
#创建对象后，python解释器默认调用__init__()方法；
#当删除一个对象时，python解释器也会默认调用一个方法，这个方法为__del__()方法


import time

print 'test1 析构'
class animals(object) :

	#初始化方法，创建对象后会自动被调用
	
	def __init__(self, name) :
		print '__init__方法被调用'
		self.__name = name

	#析构方法，当对象被删除时候，会自动被调用

	def __del__(self) :
		print '__del__方法被调用'
		print '%s对象被删除……'%self.__name

	def print_test(self) :
		print 'test code'
		

dog = animals('小花狗')

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

#私有的属性，不能通过对象直接访问，但是可以通过方法访问
#私有的方法，不能通过对象直接访问
#私有的属性、方法，不会被子类继承，也不能被访问
#一般情况下，私有的属性、方法都是不对外公布的，往往用来做内部的事情，起到安全的作用
print 'test2 单继承 '


class Animal(object):

    def __init__(self, name='动物', color='白色'):
        
        #私有变量
        self.__name = name
        self.color = color

    def __test(self):
    	
        print(self.__name)
        print(self.color)

    def test(self):
        print(self.__name)
        print(self.color)



class Dog(Animal):
    def dogTest1(self):
        #print(self.__name) #不能访问到父类的私有属性
        print(self.color)


    def dogTest2(self):
        #self.__test() #不能访问父类中的私有方法
        self.test()


A = Animal()
#print(A.__name) #程序出现异常，不能访问私有属性
print(A.color)
#A.__test() #程序出现异常，不能访问私有方法
A.test()

print("------分割线-----")

D = Dog(name = "小花狗", color = "黄色")
D.dogTest1()
D.dogTest2()




