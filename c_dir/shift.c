#include <stdio.h>

#define RES 0x4f2a

/**
 *      GPIOx->MODER  &= ~(GPIO_MODER_MODER0 << (pinpos * 2));     清除
 *    	GPIOx->MODER |= (((uint32_t)GPIO_InitStruct->GPIO_Mode) << (pinpos * 2));  置位
 */
#define SETBIT(value, num)		(value | (1 << num))   		/**< 设置某位 */
#define RESET(value, num)		(value & ~(1 << num))   	/**< 清除某位 */
#define REVBIT(value, num)		(value ^ (1 << num))   		/**< 反转某位 */
#define POWERFUNC2(x)			(1 << x)			    	/**< 2的幂次方 */
#define MULTIPLE7(value)        ((value << 3) - value) 	 	/**< 一个数的7倍 */
#define MINUS(n)				((~n) + 1)					/**< 负数 */

//#define ABS(n) 					(n ^ (n >> 31) - (n >> 31)) /**< 绝对值 */
#define ABS(n)					((n >> 31) ? ((~n) + 1) : (n))
#define AVERAGE(x, y)           ((x & y) + ((x ^ y) >> 1))   /**< 两个数的平均值 */

int func (int x) 
{
	int count = 0;
	while (x) {
		count++;
		x = x & (x - 1);
	}
	return count;
}


int main (int *argc, char *argv[])
{
    

	printf("%d \n", SETBIT(0x0, 3));
	printf("%x \n", RESET(0xff, 3));
	printf("%x \n", REVBIT(0xff, 3));
	printf("%d \n", POWERFUNC2(2));
	printf("%d \n", MULTIPLE7(3));
	printf("%d \n", MINUS(3));

	printf("ABS :%d \n", ABS(44));
	printf("%d \n", AVERAGE(4, 2));

	int count = func(8888);
	printf("8888 二进制中1 的个数 ：%d \n", count);

    return 0;
}
