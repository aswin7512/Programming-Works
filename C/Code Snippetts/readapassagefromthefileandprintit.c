/*program to read the contents in a file and print it*/
#include<stdio.h>
void main()
{
    FILE *f;
    char a;
    f=fopen("abcd","r");
    printf("THE PASSAGE IN THE FILE IS\n");
    while((a=getc(f))!=EOF)
    {
        putchar(a);
    }
    fclose(f);
}