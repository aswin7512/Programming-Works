/*program to get a passage from keyboard and save it to a file*/
#include<stdio.h>
void main()
{
    FILE *f;
    char a;
    f=fopen("abcd","w");
    printf("ENTER A PASSAGEE: ");
    while((a=getchar())!=EOF)
    {
        putc(a,f);
    }
    fclose(f);
}