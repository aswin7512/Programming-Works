//program to implement stack operations
#include<stdio.h>
#define MAXSIZE 10


int is_full(int top){
    if(top == MAXSIZE-1)
        return 1;
    else
        return 0;
}


int is_empty(int top){
    if(top == -1)
        return 1;
    else
        return 0;
}


void push(int stk[], int *top, int item){
    if(is_full(*top)){
        printf("STACK OVERFLOW\n");
    }
    else{
        stk[++(*top)] = item;
        printf("%d SUCCESSFULLY PUSHED TO STACK\n", item);
    }
}


int pop(int stk[], int *top){
    if(is_empty(*top)){
        printf("STACK UNDERFLOW\n");
    }
    else{
        return stk[(*top)--];
    }
}


int peek(int stk[], int top){
    if(is_empty(top)){
        printf("STACK EMPTY\n");
    }
    else{
        return stk[(top)];
    }
}


void display(int stk[], int top){
    if(is_empty(top))
        printf("STACK EMPTY\n");
    else{
        printf("STACK: ");
        for(int i = top; i >= 0; i--){
            printf("%d, ", stk[i]);
        }
        printf("\n");
    }
}


int main(){
    int stk[MAXSIZE], top = -1, item, ch;
    while(1){
        printf("OPERATIONS\n\
            1, PUSH\n\
            2, POP\n\
            3, PEEK\n\
            4, IS FULL\n\
            5, IS EMPTY\n\
            6, DISPLAY\n\
            7, EXIT\n\
            ENTER YOUR CHOICE(eg: Enter 1 to push): ");
        scanf("%d", &ch);
        switch(ch){
            case 1: printf("ENTER ELEMENT TO PUSH: ");
                    scanf("%d", &item);
                    push(stk, &top, item);
                    break;
            
            case 2: item = pop(stk, &top);
                    if(!is_empty(top+1))
                        printf("POPPED ELEMENT: %d\n", item);
                    break;
            
            case 3: item = peek(stk, top);
                    if(!is_empty(top))
                        printf("ELEMENT AT TOP: %d", item);
                    break;
            
            case 4: item = is_full(top);
                    if(item)
                        printf("STACK IS FULL\n");
                    else
                        printf("STACK IS NOT FULL\n");
                    break;
            
            case 5: item = is_empty(top);
                    if(item)
                        printf("STACK IS EMPTY\n");
                    else
                        printf("STACK IS NOT EMPTY\n");
                    break;
            
            case 6: display(stk, top);
                    break;
            
            case 7: return 0;

            default: printf("ENTER A VALID CHOICE\n");
        }
    }
}