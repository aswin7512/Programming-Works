/*program to find the product of 2 matrices*/
#include<stdio.h>
void main()
{
    int a[10][10],b[10][10],c[10][10],m,p,q,n,i,j,k;
    printf("ENTER NO. OF ROWS AND COLUMNS OF 1st MATRIX: ");
    scanf("%d %d",&m,&p);
    printf("ENTER NO. OF ROWS AND COLUMNS OF 2nd MATRIX: ");
    scanf("%d %d",&q,&n);
    if (p==q)
    {
        printf("ENTER ELEMENTS OF 1st MATRIX\n");
        for(i=0;i<m;i++)
        {
            for(j=0;j<p;j++)
            {
                printf("A%d%d: ",i+1,j+1);
                scanf("%d",&a[i][j]);
            }
        }
        printf("ENTER ELEMENTS OF SECOND MATRIX\n");
        for(i=0;i<q;i++)
        {
            for(j=0;j<n;j++)
            {
                printf("B%d%d: ",i+1,j+1);
                scanf("%d",&b[i][j]);
            }
        }
        for(i=0;i<m;i++)
        {
            for(j=0;j<n;j++)
            {
                c[i][j]=0;
                for(k=0;k<p;k++)
                {
                    c[i][j]+=a[i][k]*b[k][j];
                }
            }
        }
        printf("PRODUCT OF MATRIX A AND B IS\n");
        for(i=0;i<m;i++)
        {
            for(j=0;j<n;j++)
            {
                printf("%3d",c[i][j]);
            }
            printf("\n");
        }
    }
    else
    {
        printf("MULTIPLICATION NOT POSSIBLE");
    }
}