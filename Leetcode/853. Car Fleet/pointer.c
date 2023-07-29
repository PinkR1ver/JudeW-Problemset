#include<stdio.h>

int main()
{
    int num = 10;
    int* ptr = &num;

    printf("%d\n", *ptr);
    printf("%p\n", ptr);
    printf("%p\n", &num);

    *ptr = 20;

    printf("%d\n", num);

    return 0;
}