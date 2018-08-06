#include <stdio.h>

typedef union myunion {
	char a;
	int  b;
} myunion_n;


/**
 *  不能给小的数据赋值
 * 
 */
int main(int argc, char const *argv[])
{
	myunion_n u;
	u.b = 18;

	printf("sizeof() = %d \n", (unsigned int)sizeof(u));

	printf("u= %x u.a = %x u.b = %x \n", u, u.a, u.b);
	//printf("u.b = %x u.a = %x \n", u.b, u.a);
	return 0;
}