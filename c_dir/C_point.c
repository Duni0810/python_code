#include <stdio.h>
#include <string.h>

int main(void)
{
    char a[5] = {0};
    char *(*pfun)(char *, const char *);
    pfun = strcpy;

    pfun(a,"young");
    printf("%s. \n", a);
    return 0;
}
