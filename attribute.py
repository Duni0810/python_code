#coding=utf-8
#
#
#类属性和实例属性
#
#类属性的作用：
#	  可以举个例子，比如我们有一只猫的属性，每一只猫的颜色
#	都是不同的，这时候我们就定义实例属性，因为这是个体的不同，
#	但是如果知道有多少只猫，我们就需要类属性跟着类走。

# 类属性是定义在 类里面，方法外边
class Cat(object) :

	#类属性
	num = 1

	def __init__(self) :
		#市里属性
		self.age = 1
		Cat.num  += 1

	#方法
	def run(self) :
		print '猫在跑'

#这里我创建了两个对象，可以打印 num查看
#访问类属性的时候，通常用类访问
mao = Cat()
mao1 = Cat()

print 'num = ',Cat.num	
print mao.age



# 补充的类和实例属性
class People(object):
	country = 'china' #类属性

#实际上打印的是类属型内容
print(People.country)

#创建一个 对象
p = People()

#打印对象 这个也是类属性
print(p.country)

#这个实际上创建的是一个实例属性
p.country = 'japan' 

print(p.country)      #实例属性会屏蔽掉同名的类属性

print(People.country)

 #删除实例属性
del p.country   
print(p.country)

#如果需要在类外修改类属性，必须通过类对象去引用然后进行修改。
#如果通过实例对象去引用，会产生一个同名的实例属性，这种方式修改的是实例属性，
#不会影响到类属性，并且之后如果通过实例对象去引用该名称的属性，
#实例属性会强制屏蔽掉类属性，即引用的是实例属性，除非删除了该实例属性。