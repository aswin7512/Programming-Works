/*program to print colour*/
#include<stdio.h>
void main()
{
    char a;
    printf("ENTER ANY CHARACTER: ");
    scanf("%c",&a);
    if (a=='R' || a=='r')
    {
        printf("RED");
    }
    else if (a=='B' || a=='b')
    {
        printf("BLUE");
    }
    else if (a=='Y' || a=='y')
    {
        printf("YELLOW");
    }
    else
    {
        printf("NOT SPECIFIED");
    }
}