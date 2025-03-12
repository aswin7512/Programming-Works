#include<stdio.h>
void main(){
    float a,b,r;
    char op;
    printf("ENTER THE EXPRESSION IN THE FORMAT a+b: ");
    scanf("%f %c %f",&a,&op,&b);
    switch (op){
        case '+':r=a+b;
                break;
        case '-':r=a-b;
                break;
        case '*':r=a*b;
                break;
        case '/':r=a/b;
                break;
        default: printf("ENTER A VALID INPUT");
    }
    printf("%.2f %c %.2f = %.2f",a,op,b,r);
}