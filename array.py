#coding=utf-8

name = '123456789'

print '[0:3]',name[0:3] #取下标 0~2字符

print '[2:]',name[2:]  #取下标2到最后

print '[1:-1]',name[1:-1] #取下标1开始 到最后 第二个

#检测 str 是否包含在 mystr中，如果是返回开始的索引值，否则返回-1
#mystr.find(str, start=0, end=len(mystr))
#
########################(r)find####################
print '##########(r)find###########'
mystr = 'hello world itcast and itcastcpp'
print mystr.find("l")  # return 2 返回 字符l 前字符数
print mystr.find("aid") # return -1
print mystr.find("and") #return 19
print mystr.find("and", 0 ,len(mystr) -2) #在范围内查找

#################(r)index#########################
#跟find()方法一样，只不过如果str不在 mystr中会报一个异常.
#
#mystr.index(str, start=0, end=len(mystr)) 
print '##########(r)index###########'
print mystr.index("l")	 # return 2 
print mystr.rindex("l") # return 9 从右开始
#print mystr.index("and",0,10) #会报错 然后推出

############count###########################
#返回 str在start和end之间 在 mystr里面出现的次数
#mystr.count(str, start=0, end=len(mystr))
print '##########count###########'
print 'incast 出现',mystr.count("itcast"),'次'

##################replace##################
#把 mystr 中的 str1 替换成 str2,如果 count 指定，则替换不超过 count 次.
#mystr.replace(str1, str2,  mystr.count(str1))
print '##########replace###########'
print mystr.replace("it",'IT')

##################split##################
#以 str 为分隔符切片 mystr，如果 maxsplit有指定值，则仅分隔 maxsplit 个子字符串
#mystr.split(str=" ", 2)  
print '##########split###########'
print mystr.split(" ")  #用“ ” 分割 
print mystr.split(" ",1) #用字符串分割 1 次

##################capitalize##################
#把字符串的第一个字符大写
#mystr.capitalize()
print '##########capitalize###########'
print mystr.capitalize()
##################title##################
#把字符串的每个单词首字母大写
print mystr.title()

##################startswith--endswith##################
#检查字符串是否是以 obj 开头（结尾）, 是则返回 True，否则返回 False
#mystr.startswith(obj)
print '##########startswith--endswith###########'
print mystr.endswith("pp")

#################lower--upper#################
#字符串中的大小写转化
print '##########lower--upper###########'
print mystr.upper()

#################ljust-center-rjust#################
#字符串左右对其
print '##########ljust-center-rjust#################'
print mystr.rjust(50)
print mystr.center(50)

#################lstrip-strip-rstrip#################
#删除mystr字符串两端（左，右）的空白字符
test_str = "       hello   world     "
print '##########ljust-center-rjust#################'
print test_str.lstrip()  # 左
print test_str.strip()   # 两端

#################（r）partition#################
#把mystr以str分割成三部分,str前，str和str后
print '##########（r）partition#################'
print mystr.partition("world")
print mystr.rpartition("itcast")

################splitlines#################
#按照行分隔，返回一个包含各行作为元素的列表
test_str1 = "hello\nworld"
print '##########splitlines#################'
print test_str1.splitlines()

################isalpha-isdigit#################
#如果 mystr只包含数字（字母）则返回 True 否则返回 False.
print '#########isalpha-isdigit#############'
print mystr.isalpha()
print mystr.isdigit()

################isalnum#################
#如果 mystr 所有字符都是字母或数字则返回 True,否则返回 False
print '#########isalnum#############'
print mystr.isalnum()

################isspace#################
#如果 mystr 中只包含空格，则返回 True，否则返回 False.
print '#########isspace#############'
print mystr.isspace()


################join#################
#mystr 中每个字符后面插入str,构造出一个新的字符串

print '#########join#############'
str = "_"
li = ['my', 'name', 'is','young']
print str.join(li)

