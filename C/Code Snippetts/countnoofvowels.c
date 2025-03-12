/*program to count the no. of vowels in a string*/
#include<stdio.h>
#include<string.h>
void main()
{
    char a[50],v[10]="aeiouAEIOU";
    int i,j,n=0,l;
    printf("ENTER A STRING: ");
    gets(a);
    l=strlen(a);
    for(i=0;i<l;i++)
    {
        for(j=0;j<10;j++)
        {
            if (a[i]==v[j])
            {
                n+=1;
            }
        }
    }
    printf("NO. OF VOWELS IN THE STRING=%d",n);
}