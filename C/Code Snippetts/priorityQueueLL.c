#include<stdio.h>
#include<stdlib.h>

struct Pque {
    int data;
    int priority;
    struct Pque* next;
};

struct Pque* initNode(int datum, int pri) {
    struct Pque* newnode = (struct Pque*) malloc(sizeof(struct Pque));
    newnode->data = datum;
    newnode->priority = pri;
    newnode->next = NULL;
    return newnode;
}

void enqueue(struct Pque** front, struct Pque** rear, int datum, int pri) {
    struct Pque* newnode = initNode(datum, pri);
    
    if (*front == NULL) {
        *front = *rear = newnode;
    } else {
        struct Pque *temp = *front, *before = NULL;

        while (temp != NULL && temp->priority <= pri) {
            before = temp;
            temp = temp->next;
        }

        if (before == NULL) {
            newnode->next = *front;
            *front = newnode;
        } else {
            newnode->next = before->next;
            before->next = newnode;
            if (newnode->next == NULL) {
                *rear = newnode;
            }
        }
    }
}

int dequeue(struct Pque** front, struct Pque** rear) {
    int item = -999;
    if (*front == NULL) {
        printf("Queue Empty, Cannot delete element!!!\n");
    } else {
        struct Pque* temp = *front;
        item = temp->data;
        *front = (*front)->next;
        free(temp);
        if (*front == NULL) {
            *rear = NULL;
        }
    }
    return item;
}

void display(struct Pque* front, struct Pque* rear) {
    if (front == NULL) {
        printf("Queue Empty, No Elements to display!!!\n");
    } else {
        struct Pque* temp = front;
        printf("Queue: ");
        while (temp != NULL) {
            printf("(%d, %d) ", temp->data, temp->priority);
            temp = temp->next;
        }
        printf("\n");
    }
}

int main() {
    struct Pque *front = NULL, *rear = NULL;
    int item, pri, ch;
    while (1) {
        printf("Operations\n\
                0. Exit\n\
                1. Enqueue\n\
                2. Dequeue\n\
                3. Display\n\
                Enter your choice: ");
        scanf("%d", &ch);
        switch (ch) {
            case 0: printf("Aborting Program...\n");
                    return 0;
            
            case 1: printf("Enter Item to Enqueue and its Priority: ");
                    scanf("%d %d", &item, &pri);
                    enqueue(&front, &rear, item, pri);
                    break;
            
            case 2: item = dequeue(&front, &rear);
                    if (item != -999)
                        printf("Dequeued Element: %d\n", item);
                    break;
            
            case 3: display(front, rear);
                    break;
            
            default: printf("Please Enter A Valid Choice...\n");
        }
    }
}
