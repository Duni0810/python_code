#include <stdio.h>


typedef struct mystruct
{
	char a : 1;
	char b : 1;
    int  c : 1;
} mystruct1_t;

typedef struct mystruct1
{
    char a;
    char b;
    int c;

} mystruct2_t;


int main(int argc, char const *argv[])
{
	mystruct1_t mystr;
    mystruct2_t mystr1;
	printf("sizeof(mystr) = %d \t sizeof(mystr1) = %d \n",(int)sizeof(mystr),
                                                          (int)sizeof(mystr1));

	return 0;
}
