#coding=utf-8

# 面向对象编程
# 这个类似与 C中的结构体
# 说说概念：
# 例如： 学生是一个大类
# 		 young是一个学生 这个young是对象
# 		 young的衣服是蓝色的 这个是对象的属性
#
#为什么要面向对象呢？
#很多东西他们都给你封装好了，可以直接调用，比较方便
#下面来创建一个简单的面向对象
#
#
#关于self 的理解
#所谓的self，可以理解为自己
#可以把self当做C++中类里面的this指针一样理解，就是对象自身的意思
#某个对象调用其方法时，python解释器会把这个对象作为第一个参数传递给self，所以开发者只需要传递后面的参数即可

class student :

	#这个是对象初始化， 每次新建对象的时候都会自动调用
	def __init__(self, name, sex) :
		self.name = name
		self.sex = sex

	#当使用print输出对象的时候，只要自己定义了__str__(self)方法，那么就会打印从在这个方法中return的数据
	def __str__(self) :
		return 'hahah'

	def print_info(self) :
		print 'my name is : ',self.name
		print self.sex



young = student('young','m')
young.print_info()

# 这里我们修改属性用 方法来进行修改，尽量避免直接修改
leos = student('leos', 'm')
leos.print_info()

print young


# 以上的属性都属于公有类，但是这样不安全，为了更好的保存属性安全，即不能随意修改，一般的处理方式为将属性定义为私有属性
#添加一个可以调用的方法，供调用
#
class people(object) :

#初始化
	def __init__(self, name) :
		self.__name = name 

#获取名字
	def getname(self) :
		return self.name

#设置名字
	def setname(self, newName) :
		if len(newName) >= 5 :
			self.__name = newName

		else :
			print 'err:名字必须长度大于5'

xiaoming = people('young')
print xiaoming.name
