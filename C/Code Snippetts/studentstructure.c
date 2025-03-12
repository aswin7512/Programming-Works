/*program to input the register number and marks of 3 subjects of n students and display the total marks of the student*/
#include<stdio.h>
void main()
{
    struct student{
        int r;
        int m1;
        int m2;
        int m3;
        int t;
    }s[50];
    int n,i;
    printf("ENTER THE NUMBER OF STUDENTS: ");
    scanf("%d",&n);
    for(i=0;i<n;i++)
    {
        printf("ENTER REGISTER NUMBER AND 3 MARKS OF THE STUDENT: ");
        scanf("%d %d %d %d",&s[i].r,&s[i].m1,&s[i].m2,&s[i].m3);
        s[i].t=s[i].m1+s[i].m2+s[i].m3;
        printf("TOTAL MARKS OF STUDENT= %d\n",s[i].t);
    }
}