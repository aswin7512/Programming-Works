//program to implement circular Queue
#include<stdio.h>
#define MAXSIZE 10


int is_full(int front, int rear){
    if((rear + 1) % MAXSIZE == front)
        return 1;
    return 0;
}


int is_empty(int front){
    if(front == -1)
        return 1;
    return 0;
}


int enqueue(int que[], int *front, int *rear, int item){
    if(is_full(*front, *rear))
        return 0;
    else if(is_empty(*front))
        (*front)++;
    else if(*rear == MAXSIZE-1)
        *rear = -1;
    que[++(*rear)] = item;
    return 1;
}


int dequeue(int que[], int *front, int *rear){
    if(is_empty(*front))
        return -9999;
    int item = que[(*front)++];
    if(*front - *rear == 1)
        *front = *rear = -1;
    if(*front == MAXSIZE)
        *front = 0;
    return item;
}


void display(int que[], int front, int rear){
    int cnt;
    if(is_empty(front))
        printf("QUEUE IS EMPTY :(\n");
    else{
        printf("QUEUE: ");
        cnt =front > rear? (MAXSIZE - front + rear) + 1 :rear - front + 1;
        for(int i = front, j = 0; j < cnt; i++, j++){
            if(i == MAXSIZE)
                i = 0;
            printf("%d, ", que[i]);
        }
        printf("\n");
    }
}


int main(){
    int que[MAXSIZE], front = -1, rear = -1, ch, item;
    while(1){
        printf("OPERATIONS\n\
                1. ENQUEUE\n\
                2. DEQUEUE\n\
                3. IS FULL\n\
                4. IS EMPTY\n\
                5. DISPLAY\n\
                0. EXIT\n\
                ENTER YOUR CHOICE: ");
        scanf("%d", &ch);
        switch(ch){
            case 1: printf("ENTER ELEMENT TO ENQUEUE: ");
                    scanf("%d", &item);
                    int st = enqueue(que, &front, &rear, item);
                    if(st)
                        printf("%d SUCCESSFULLY ENQUEUED :)\n", item);
                    else
                        printf("QUEUE IS FULL, ENQUEUE NOT POSSIBLE :(\n");
                    break;
            
            case 2: item = dequeue(que, &front, &rear);
                    if(item != -9999)
                        printf("DEQUEUED ELEMENT: %d\n", item);
                    else
                        printf("QUEUE IS EMPTY NO ELEMENTS TO DEQUEUE :(\n");
                    break;
            
            case 3: item = is_full(front, rear);
                    if(item)
                        printf("QUEUE IS FULL :)\n");
                    else
                        printf("QUEUE IS NOT FULL :(\n");
                    break;
            
            case 4: item = is_empty(front);
                    if(item)
                        printf("QUEUE IS EMPTY :)\n");
                    else
                        printf("QUEUE IS NOT EMPTY :(\n");
                    break;
            
            case 5: display(que, front, rear);
                    break;
            
            case 0: printf("ABORTING... :)\n");
                    return 0;

            default: printf("PLEASE ENTER A VALID CHOICE!!!\n");
        }
    }
}