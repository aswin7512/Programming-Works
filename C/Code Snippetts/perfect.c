#include<stdio.h>
int main(){
    int a,s=0;
    printf("ENTER A NUMBER: ");
    scanf("%d",&a);
    for(int i=1;i<a;i++){
        if(a%i==0){
            s+=i;
        }
    }
    s==a?printf("%d is a perfect number",a):printf("%d is not a perfect number",a);
    return 0;
}