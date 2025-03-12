/*program to check whether a sting is palindrome or not*/
#include<stdio.h>
#include<string.h>
void main()
{
    char a[50];
    int i=0,j,p=1;
    printf("ENTER A STRING: ");
    gets(a);
    j=strlen(a)-1;
    while (i<j)
    {
        if (a[i]!=a[j])
        {
            p=0;
            break;
        }
        i+=1;
        j-=1;
    }
    if (p)
    {
        printf("STRING IS PALINDROME");
    }
    else
    {
        printf("STRING IS NOT PALINDROME");
    }
}