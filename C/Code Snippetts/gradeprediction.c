/*program to print grade*/
#include<stdio.h>
void main()
{
    int a;
    float b,c,d,p;
    printf("ENTER REGISTER NUMBER AND MARKS: ");
    scanf("%d %f %f %f",&a,&b,&c,&d);
    p=((b+c+d)/300)*100;
    if (b<40 || c<40 || d<40)
    {
        printf("FAILED");
    }
    else if (p>75)
    {
        printf("DISTINCTION");
    }
    else if (p>=60)
    {
        printf("FIRST CLASS");
    }
    else if (p>=50)
    {
        printf("SECOND CLASS");
    }
    else
    {
        printf("THIRD CLASS");
    }
}
