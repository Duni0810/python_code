#include <stdio.h>
#include "framework.h"

int sum (int a, int b) 
{
	return (a + b);
}

int sub (int a, int b)
{
	return (a - b);
}

int multiply (int a, int b)
{
	return (a * b);
}

int divide (int a, int b)
{
	return (a / b);
}

int main(int argc, char const *argv[])
{
	int ret = 0;
	cal_t mycal;			/* 定义一个函数指针 */

	mycal.a = 12;
	mycal.b = 2;
	mycal.cal_p = sum;		/* 函数指针赋值 */

	ret = calulator (&mycal);

	printf("ret = %d\n", ret);
	return 0;
}