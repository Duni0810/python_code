objects = C_framework.o framework.o    # 项目文件
CC = gcc                               # 全局定义  类似 define

a.out : $(objects)                     # 目标
	$(CC) -o a.out $(objects)

C_framework.o : C_framework.c   #让GNU自动推倒 .o 文件   依赖    
framework.o : framework.c

.PHONY : clean
clean:
	rm a.out $(objects) -rf 
	clear
	ls
