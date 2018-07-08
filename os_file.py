#coding=utf-8

#有些时候，需要对文件进行重命名、删除等一些操作，python的os模块中都有这么功能
import os

#1.文件重命名
#os模块中的rename()可以完成对文件的重命名操作
#格式rename(需要修改的文件名, 新的文件名)

#在这个文件夹下创建一个test.txt文件做测试
os.rename('test.txt', 'young1.txt')
print 'rename ok'

#删除文件
os.remove('young1.txt')
print 'remove ok'

#创建文件夹
os.mkdir('youngdir')
print 'add dir ok'

#删除文件夹
os.rmdir('youngdir')
print 'del dir ok'

#获取当前目录列表
print os.listdir('./')

#获取当前目录
print os.getcwd()

#改变目录 例子是返回上一级目录
os.chdir('../')

#获取当前目录
print os.getcwd()



