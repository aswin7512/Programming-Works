/*program to check whether a number exists in the array*/
#include<stdio.h>
void main()
{
    int a[100],n,s,i;
    printf("ENTER NUMBER OF ELEMENTS: ");
    scanf("%d",&n);
    for(i=0;i<n;i++)
    {
        printf("ENTER NUMBER %d",i+1);
        scanf("%d",&a[i]);
    }
    printf("ENTER NUMBER TO SEARCH: ");
    scanf("%d",&s);
    for(i=0;i<n;i++)
    {
        if(s==a[i])
        {
            printf("NUMBER FOUND");
            goto k;
        }
    }
    printf("NUMBER NOT FOUND");
    k: ;
}