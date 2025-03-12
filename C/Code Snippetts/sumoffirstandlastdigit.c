#include<stdio.h>
void main(){
    int a,n,s=0,c;
    printf("ENTER A NUMBER: ");
    scanf("%d",&a);
    c=a;
    n=a%10;
    s+=n;
    n/=10;
    while(a!=0){
        if (a<10){
            n=a%10;
            s+=n;
        }
        a/=10;
    }
    printf("SUM OF FIRST AND LAST DIGITS OF %d IS %d",c,s);
}