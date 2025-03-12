/*program to print no. of days in the month*/
#include<stdio.h>
void main()
{
    int a,b;
    printf("ENTER THE NUMERICAL VALUE OF THE MONTH AND YEAR: ");
    scanf("%d %d",&a,&b);
    switch (a)
    {
        case 1:
        case 3:
        case 5:
        case 7:
        case 8:
        case 10:
        case 12:printf("31 days");
              break;

        case 4:
        case 6:
        case 9:
        case 11:printf("30 days");
               break;

        case 2:if (b%4==0)
            {
            printf("29 days");
            }
            else
            {
            printf("28 days");
            }
            break;

        default:printf("INVALID CHOICE");
    }
}