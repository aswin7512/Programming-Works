/*program to store register number and 3 marks in a file*/
#include<stdio.h>
void main()
{
    FILE *f;
    int r,a,b,c;
    f=fopen("marks.txt","w");
    printf("ENTER REGISTER NUMBER AND 3 MARKS OF THE STUDENT: ");
    scanf("%d %d %d %d",&r,&a,&b,&c);
    fprintf(f,"%d, %d, %d, %d",r,a,b,c);
    fclose(f);
}