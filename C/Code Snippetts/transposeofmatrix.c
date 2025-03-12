/*program to find the transpose of a matrix*/
#include<stdio.h>
void main()
{
    int a[10][10],b[10][10],i,j,m,n;
    printf("ENTER THE NO. OF ROWS AND COLUMNS: ");
    scanf("%d %d",&m,&n);
    printf("ENTER THE ELEMENTS OF THE MATRIX\n");
    for(i=0;i<m;i++)
    {
        for(j=0;j<n;j++)
        {
            printf("ENTER ELEMENT A%d%d: ",i+1,j+1);
            scanf("%d",&a[i][j]);
        }
    }
    for(i=0;i<m;i++)
    {
        for(j=0;j<n;j++)
        {
            b[j][i]=a[i][j];
        }
    }
    printf("INITIAL MATRIX\n");
    for(i=0;i<m;i++)
    {
        for(j=0;j<n;j++)
        {
            printf("%3d",a[i][j]);
        }
    printf("\n");
    }
    printf("\nFINAL MATRIX\n");
    for(i=0;i<n;i++)
    {
        for(j=0;j<m;j++)
        {
            printf("%3d",b[i][j]);
        }
    printf("\n");
    }
}