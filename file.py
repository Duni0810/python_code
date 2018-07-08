#coding=utf-8

# 其实python中关于文件操作和 C 差不多
# r	以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
#w	打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
#a	打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。

f = open('hello.py', 'a')
f.write('#test code\n') 
f.close()#这个必须是一对的 打开必须有关闭

# 读数据有三种
# 1.read
# 使用read(num)可以从文件中读取数据，num表示要从文件中读取的数据的长度（单位是字节），
# 如果没有传入num，那么就表示读取文件中所有的数据
print '===read()==='
f = open('hello.py', 'r')
print f.read(5)
print '='*20
print f.read()   			# 这里有一个读取指针的问题，后面会解释
f.close()
# 2.readline
print '===readline()==='
f = open('hello.py', 'r')
print '1:',f.readline()		#只要文件不关闭，指针会指向下一个地址
print '2:',f.readline()
print '3:',f.readline()
print '4:',f.readline()
print 'type(f.read)',type(f.read())				#这个类型是str 字符串
print 'type(f.readline)',type(f.readline())		#这个类型是str 字符串
print 'type(f.readlines)',type(f.readlines())	##这个类型是list 列表
f.close()

# 3.readlines
#
print '===readlines==='
f = open('hello.py', 'r')
print 'f.readlines()',f.readlines()
f.close()


