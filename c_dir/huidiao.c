#include <stdio.h>

/* function*/
int function (int a)
{
    return (a * a);
}

/* function2 */
int function2 (int a)
{
    return (a * a * a);
}

/**
 *	param : int (*p)(int)  函数名
 *			a              函数参数
 */
int huidiao(int (* p)(int), int arg)
{
    return p(arg);

}
 

int main(int argc, char *argv[])
{
    
    int x = huidiao(function,  4);	 /* 同步回调 */ 
    int y = huidiao(function2, 4);   /* 同步回调 */

    /* 测试打印 */
    printf("sizeof(char)   = %ld , sizeof(int)   = %ld  \n", sizeof(char),   sizeof(int));
    printf("sizeof(char *) = %ld , sizeof(int *) = %ld .\n", sizeof(char *), sizeof(int *));

    printf("sizeof(function) = %ld \t sizeof(huidiao) = %ld \n", sizeof(&function), sizeof(&huidiao));
    printf("x = %d  y = %d .\n", x, y);

    return 0;
}
