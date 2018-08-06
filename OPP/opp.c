#include "opp.h"

/**
 * 私有变量
 */
struct info
{
	char tel[11];
};

/*
 * 子类测试函数
 */
static void print_student(student_t *__this)
{
	printf("this is student .\n");
}

/**
 * 父类测试函数
 */
static void print_people(people_t *__this)
{
	printf("this is people .\n");
}

/**
 * 访问私有变量函数
 */
static void change_tel(struct student *__this, const char *str)
{
	strcpy(__this->msg->tel, str);
}

/**
 * 访问私有量函数
 */
static void get_tel(struct student *__this)
{
	printf("tel :%s \n",__this->msg->tel);
}

/**
 * 构造 student 对象
 */
student_t *new_student()
{
	student_t *p = malloc(sizeof(student_t));

	p->score = 0;
	p->func_student = print_student;
	p->__this = p;

	p->msg = malloc(sizeof(info_t));
	((people_t *)p)->func_people = print_people;
	p->func_settel = change_tel;
	 p->func_gettel = get_tel;

	return p;
}

/**
 * 构造 person 对象
 */
people_t *new_people()
{
	people_t *p = malloc(sizeof(people_t));

	p->age  = 0;
	strcpy(p->name, "");
	p->func_people = print_people;
	p->__this = p;

	return p;
}

