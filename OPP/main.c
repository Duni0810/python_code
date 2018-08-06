#include <stdio.h>
#include "opp.h"

int main(int argc, int *argv[]) 
{

	student_t *p = new_student();					//构造

	printf("student: %d \n", p->score);
	//printf("this:%d \n", p->__this->score);		// this指针

	p->func_student(p);

	((people_t *)p)->func_people(((people_t *)p)->__this);

	p->func_settel(p, "3312");
	p->func_gettel(p);

	return 0;
}

