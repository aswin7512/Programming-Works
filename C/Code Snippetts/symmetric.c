/*program to check whether a matrix is symmetric or not*/
#include<stdio.h>
void main()
{
    int a[10][10],b[10][10],i,j,n,s=1;
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
        for(j=0;j<n;j++)
        {
            b[i][j]=a[j][i];
        }
    }
    for(i=0;i<n;i++)
    {
        for(j=0;j<n;j++)
        {
            if(a[i][j]!=b[i][j])
            {
                s=0;
                goto k;
            }
        }
    }
    k:;
    if (s==1)
    {
        printf("MATRIX IS SYMMETRIC");
    }
    else
    {
        printf("MATRIX IS NOT SYMMETRIC");
    }
}