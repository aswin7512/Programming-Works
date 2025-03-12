//program to find the sum of 2 numbers using command line argument
#include<stdio.h>
#include<stdlib.h>
void main(int argc,char *argv[])
{
    int a,b,s;
    a=atoi(argv[1]);
    b=atoi(argv[2]);
    s=a+b;
    printf("SUM=%d",s);
}