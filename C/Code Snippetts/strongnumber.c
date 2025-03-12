#include<stdio.h>
int main(){
    int a,r,c,f,s=0;
    printf("ENTER A NUMBER: ");
    scanf("%d",&a);
    c=a;
    while(a!=0){
        r=a%10;
        f=1;
        for(int i=1;i<=r;i++){
            f*=i;
        }
        s+=f;
        a/=10;
    }
    c==s?printf("%d is strong",c):printf("%d is not strong",c);
    return 0;
}