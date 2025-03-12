#include<stdio.h>
void main(){
    int a,i;
    printf("ENTER A NUMBER: ");
    scanf("%d",&a);
    for(i=2;i<a;i++){
        if(a%i==0){
            break;
        }
    }
    i!=a?printf("%d is composite",a):printf("%d is prime",a);
}