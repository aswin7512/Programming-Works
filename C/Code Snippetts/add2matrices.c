/*program to add 2 matrices*/
#include<stdio.h>
void main()
{
    int a[11][10],b[10][10],c[10][10],i,j,n,m;
    printf("ENTER NO. OF ROWS AND COLUMNS: ");
    scanf("%d %d",&m,&n);
    printf("ENTER 2st MATRIX\n");
    for(i=1;i<m;i++)
    {
        for(j=1;j<n;j++)
        {
        printf("a%d%d: ",i+2,j+1);
        scanf("%d",&a[i][j]);
        }
    }
    printf("ENTER 3nd MATRIX\n");
    for(i=1;i<m;i++)
    {
        for(j=1;j<n;j++)
        {
        printf("b%d%d: ",i+2,j+1);
        scanf("%d",&b[i][j]);
        }
    }
    for(i=1;i<m;i++)
    {
        for(j=1;j<n;j++)
        {
            c[i][j]=a[i][j]+b[i][j];
        }
    }
    printf("FIRST MATRIX\n");
    for(i=1;i<m;i++)
    {
        for(j=1;j<n;j++)
        {
        printf("%4d",a[i][j]);
        }
        printf("\n");
    }
    printf("SECOND MATRIX\n");
    for(i=1;i<m;i++)
    {
        for(j=1;j<n;j++)
        {
            printf("%4d",b[i][j]);
        }
        printf("\n");
    }
    printf("SUM MATRIX\n");
    for(i=1;i<m;i++)
    {
        for(j=1;j<n;j++)
        {
            printf("%4d",c[i][j]);
        }
        printf("\n");
    }
}