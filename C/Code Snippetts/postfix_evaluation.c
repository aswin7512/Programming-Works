#include<stdio.h>
#include<ctype.h>
#include<math.h>
#define MAXSIZE 30

void push(float stk[], int* top, float item) {
    if(*top != MAXSIZE)
        stk[++(*top)] = item;
}

float pop(float stk[], int* top) {
    if(*top != -1)
        return stk[(*top)--];
    return -999;
}

float peek(float stk[], int top) {
    if(top != -1)
        return stk[top];
    return -999;
}

float post_eval(char post[]){
    float stk[MAXSIZE],a, b, result;
    int top = -1;
    for(int i = 0; post[i] != '\0'; i++){
        if(isdigit(post[i]))
            push(stk, &top, post[i] - 48);
        else{
            b = pop(stk, &top);
            a = pop(stk, &top);
            switch(post[i]){
                case '+': result = a + b;
                        break;
                case '-': result = a - b;
                        break;
                case '*': result = a * b;
                        break;
                case '/': result = a / b;
                        break;
                case '^': result = pow(a, b);
                        break;
            }
            push(stk, &top, result);
        }
    }
    return pop(stk, &top);
}

int main(){
    char post[MAXSIZE];
    float r;
    printf("ENTER A POSTFIX EXPRESSION: ");
    scanf("%[^\n]%*c", post);
    r = post_eval(post);
    printf("%s = %f", post, r);
    return 0;
}