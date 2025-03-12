/*program to read register number and 3 marks from file and print it*/
#include<stdio.h>
void main()
{
    FILE *f;
    int r,a,b,c;
    f=fopen("marks.txt","r");
    printf("%20s %10s %10s %10s\n\n","REGISTER NUMBER","MARK 1","MARK 2","MARK 3");
    fscanf(f,"%d, %d, %d, %d",&r,&a,&b,&c);
    printf("%20d %10d %10d %10d",r,a,b,c);
    fclose(f);
}