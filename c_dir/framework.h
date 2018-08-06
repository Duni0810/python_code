#ifndef __FUNC__
#define __FUNC__

#include <stdio.h>

typedef int (*cal_punc)(int , int); /**< 返回值为int 类型，参数为 两个int 类型 */

typedef struct cal {
	int a;
	int b;
	cal_punc cal_p;	/**< 定义一个函数指针 */
}cal_t;


/**
 * 计算器的功能函数
 */
int calulator (cal_t *p1);   /**< 传入一个结构体指针 */

#endif