#include <stdio.h>

/**
 *  用typedef定义一个函数指针类型
 */
typedef int (*pfunc)(int, int );

/**
 * 加
 */
int sum (int a, int b) 
{
	return (a + b);
}

/**
 * 减
 */
int sub (int a, int b)
{
	return (a - b);
}

/**
 * 乘
 */
int multiply (int a, int b)
{
	return (a * b);
}

/**
 * 除
 */
int divide (int a, int b)
{
	return (a / b);
}

int main(int argc, char const *argv[])
{
	pfunc p1 = NULL;	 /* 定义一个函数指针 */
	int a = 0, b = 0, result = 0;
	char c = 0;

	printf("输入a, b 的数值\n");
	scanf("%d %d",&a, &b);

	printf("输入符号c:+ | - | * | / \n");
	
	c = getchar();

	/* 我们在输入时候，都是用‘\n’结尾，但是程序中scanf不会去接收 \n */
	do
	{
		scanf("%c", &c);
	} while (c == '\n');

	switch (c) {
		case '+' : p1 = sum; break;
		case '-' : p1 = sub; break;
		case '*' : p1 = multiply; break;
		case '/' : p1 = divide; break;

		default : break;
	}
    
    result = p1(a, b);
    printf("%d %c %d = %d\n", a, c , b , result);


	return 0;
}
