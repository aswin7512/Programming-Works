/*program to find the sum difference product and quotient using function*/
#include<stdio.h>
void main()
{
    int sum(int,int);
    int diff(int,int);
    int product(int,int);
    int quotient(int,int);
    int a,b,s,d,p,q;
    printf("ENTER ANY 2 NUMBERS: ");
    scanf("%d %d",&a,&b);
    s=sum(a,b);
    d=diff(a,b);
    p=product(a,b);
    q=quotient(a,b);
    printf("SUM=%d\nDIFFERENCE=%d\nPRODUCT=%d\nQUOTIENT=%d",s,d,p,q);
}
int sum(int a,int b)
{
    return a+b;
}
int diff(int a,int b)
{
    return a-b;
}
int product(int a,int b)
{
    return a*b;
}
int quotient(int a,int b)
{
    return a/b;
}