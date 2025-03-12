//program to find the nCr value of a given combination
#include<stdio.h>
int fact(int a){
    int f=1;
    for(int i=1;i<=a;i++){
        f*=i;   // f=f*i
    }
    return f;
}
int main(){
    int n,r,c,f1,f2,f3;
    printf("ENTER VALUE OF n AND r: ");
    scanf("%d %d",&n,&r);
    printf("%d\n",fact(0));
    f1=fact(n);
    f2=fact(n-r);
    f3=fact(r);
    c=f1/(f2*f3);
    printf("nCr VALUE OF THE GIVEN COMBINATION IS %d",c);
    return 0;
}