//program to find the product of 2 matrices
#include<stdio.h>
void main()
{
    int a[10][10],b[10][10],c[10][10],i,j,k,m,n,o,p;
    printf("ENTER THE NUMBER OF ROWS AND COLUMNS OF THE FIRST MATRIX: ");
    scanf("%d %d",&m,&o);
    printf("ENTER THE NUMBER OF ROWS AND COLUMNS OF THE SECOND MATRIX: ");
    scanf("%d %d",&p,&n);
    if (o==p)
    {
        printf("MULTIPLICATION POSSIBLE\n");
        printf("ENTER THE ELEMENTS OF MATRIX A\n");
        for(i=0;i<m;i++)
        {
            for(j=0;j<o;j++)
            {
                printf("ENTER ELEMENT A%d%d: ",i+1,j+1);
                scanf("%d",&a[i][j]);
            }
        }
        printf("ENTER ELEMENTS OF MATRIX B\n");
        for(i=0;i<p;i++)
        {
            for(j=0;j<n;j++)
            {
                printf("ENTER ELEMENT B%d%d: ",i+1,j+1);
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
        printf("MATRIX A IS\n");
        for(i=0;i<m;i++)
        {
            for(j=0;j<o;j++)
            {
                printf("%4d",a[i][j]);
            }
            printf("\n");
        }
        printf("MATRIX B IS\n");
        for(i=0;i<p;i++)
        {
            for(j=0;j<n;j++)
            {
                printf("%4d",b[i][j]);
            }
            printf("\n");
        }
        printf("PRODUCT OF A AND B IS\n");
        for(i=0;i<m;i++)
        {
            for(j=0;j<n;j++)
            {
                printf("%4d",c[i][j]);
            }
            printf("\n");
        }
    }
    else
    {
        printf("MULTIPLICATION NOT POSSIBLE");
    }
}