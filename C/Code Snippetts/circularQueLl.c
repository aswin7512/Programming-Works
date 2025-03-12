//program to implement circular queue using linked list
#include<stdio.h>
#include<stdlib.h>

struct Que {
    int data;
    struct Que* next;
} Que;

struct Que* initNode(int datum) {
    struct Que* newnode = (struct Que*) malloc(sizeof(Que));
    newnode->data = datum;
    newnode->next = NULL;
}

int isEmpty(struct Que* rear) {
    if (rear == NULL)
        return 1;
    return 0;
}

void enqueue(int datum, struct Que** front, struct Que** rear) {
    struct Que* newnode = initNode(datum);
    if (isEmpty(*rear))
        *front = *rear = newnode->next = newnode;
    else {
        (*rear)->next = newnode;
        *rear = newnode;
        newnode->next = *front;
    }
}

int dequeue(struct Que** front, struct Que** rear) {
    int item;
    if (isEmpty(*rear))
        item = -999;
    else {
        item = (*front)->data;
        if (*front == * rear)
            *front = *rear = NULL;
        else {
            *front = ((*front)->next);
            (*rear)->next = *front;
        }
    }
    return item;
}

int peek(struct Que** front) {
    if (isEmpty(*front))
        return -999;
    else
        return (*front)->data;
}

void display(struct Que** front, struct Que** rear) {
    if (isEmpty(*rear))
        printf("Queue Empty\n");
    else {
        struct Que* temp = *front;
        do {
            printf("%d, ", temp->data);
            temp = temp->next;
        } while (temp != *front);
        printf("\n");
    }
}

int main(){
    struct Que *front = NULL, *rear = NULL;
    int item, ch;
    while (1) {
        printf("Operations:\n\
        0. Exit\n\
        1. Enqueue\n\
        2. Dequeue\n\
        3. Peek\n\
        4. Is Empty\n\
        5. Display\n\
        Enter your choice: ");
        scanf("%d", &ch);
        switch(ch) {
            case 0: return 0;
            case 1: printf("Enter Item to Enqueue: ");
                    scanf("%d", &item);
                    enqueue(item, &front, &rear);
                    break;
            case 2: item = dequeue(&front, &rear);
                    if(item != -999)
                        printf("Deleted Item: %d\n", item);
                    else
                        printf("Queue Empty\n");
                    break;
            case 3: item = peek(&front);
                    if (item != -999)
                        printf("Item at Front: %d\n", item);
                    else
                        printf("Queue Empty\n");
            case 4: if (isEmpty(rear))
                        printf("Queue Empty\n");
                    else
                        printf("Queue Not Empty\n");
                    break;
            case 5: display(&front, &rear);
                    break;
            default: printf("Please Enter a Valid Choice!!!\n");
        }
    }
}