/*program to calculate the sum of the diagonal elements of a square matrix*/
#include<stdio.h>
void main()
{
    int a[10][10],i,j,n,s=0;
    printf("ENTER THE ORDER OF THE MATRIX: ");
    scanf("%d",&n);
    printf("ENTER THE ELEMENTS OF THE MATRIX\n");
    for(i=0;i<n;i++)
    {
        for(j=0;j<n;j++)
        {
            printf("ENTER ELEMENT A%d%d: ",i+1,j+1);
            scanf("%d",&a[i][j]);
        }
    }
    for(i=0;i<n;i++)
    {
        s+=a[i][i];
    }
    printf("SUM OF THE DIAGONAL ELEMENTS IS %d",s);
}