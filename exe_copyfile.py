#coding=utf-8
#该功能是做一个文件的拷贝功能，拷贝文件名字为 xxx[copy].py


oldfilename = raw_input("输入你要拷贝的文件：")

#1.打开要复制的文件
oldfile = open(oldfilename , 'r')

#2. 创建一个新的文件，用来存储源文件的数据内容
if oldfile :														# 判断文件是否打开成功
	print 'open ok'
	file_flag_num = oldfilename.rfind('.') 							# c从字符串的右边起找到文件的‘.’，返回位置
	if file_flag_num > 0:
		temp = oldfilename[file_flag_num:] 							# 这里用到的是之前的字符串切片

	newfilename = oldfilename[:file_flag_num] + '[copy]' + temp		# 字符串的处理
	#print newfilename												# 测试文件名字是否正确
	newfile = open(newfilename, 'w')								# 创建文件名字

#3. 复制
#这里的复制有一个问题，为什么我们不选择用read()或者用readlines呢？
#就是如果文件特别大，这种方式特别不安全。所以采用读一行，写一行的方式
	while True :
		linecontent = oldfile.readline()
		if len(linecontent) > 0 :
			newfile.write(linecontent)
		else :
			break
#4. 关闭文件
	newfile.close()


oldfile.close()


