/*program to print colour*/
#include<stdio.h>
void main()
{
    char a;
    printf("ENTER ANY CHARACTER: ");
    scanf("%c",&a);
    switch (a)
    {
        case 'R':
        case 'r':printf("RED");
            break;

        case 'B':
        case 'b':printf("BLUE");
             break;

        case 'Y':
        case 'y':printf("YELLOW");
             break;

        default:printf("INVALID");
    }
}