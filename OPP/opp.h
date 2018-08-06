#ifndef __OPP_H_
#define __OPP_H_

#include <stdio.h>
#include <string.h>
#include <malloc.h>

typedef struct info info_t;

typedef struct people
{
	char name[20];
	int  age;

	struct people *__this;
	void (* func_people)(struct people *__this);	//得绑定一个函数

}people_t;

typedef struct student
{
	people_t parent;								// 继承
	int score;

	struct info *msg;

	struct student *__this;
	void (* func_student)(struct student *__this);
	void (* func_settel)(struct student *__this, const char *str);
	void (* func_gettel)(struct student *__this);
}student_t;


student_t *new_student();

people_t *new_people();


#endif
