#include <stdio.h>
#include <string.h>


struct person {
	char name[20];
	int age;
};

struct student {
	struct person p;	// 继承person类
	int score;
};

void function (struct person * p1)
{
	strcpy(p1->name, "young");
	p1->age = 10;
	((struct student *)p1)->score = 100;
}

void main ()
{
	struct student p1;

	function((struct person *)&p1);
	
	printf(" age = %d   name = %s score = %d\n", p1.p.age, p1.p.name, p1.score); 
}




