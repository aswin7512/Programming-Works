#include<stdio.h>
void main(){
    int a;
    printf("ENTER A NUMBER: ");
    scanf("%d",&a);
    a%2==0?printf("EVEN"):printf("ODD");
}