#include <stdio.h>
#include <stdlib.h>
#define MAXSIZE 100 // Maximum size of the queue

// Function definitions

// Function to add an element to the queue
void enqueue(int* queue, int* front, int* rear, int value) {
    if (*rear == MAXSIZE - 1) {
        printf("Queue Overflow! Cannot enqueue.\n");
    } else {
        if (*front == -1) // If queue is initially empty
            *front = 0;
        (*rear)++;
        queue[*rear] = value;
        printf("%d enqueued to the queue.\n", value);
    }
}

// Function to remove an element from the queue
void dequeue(int* queue, int* front, int* rear) {
    if (*front == -1 || *front > *rear) {
        printf("Queue Underflow! Cannot dequeue.\n");
    } else {
        printf("%d dequeued from the queue.\n", queue[*front]);
        (*front)++;
        if (*front > *rear) { // Reset the queue when empty
            *front = *rear = -1;
        }
    }
}

// Function to display the elements of the queue
void display(int* queue, int front, int rear) {
    if (front == -1 || front > rear) {
        printf("Queue is empty.\n");
    } else {
        printf("Queue elements: ");
        for (int i = front; i <= rear; i++) {
            printf("%d ", queue[i]);
        }
        printf("\n");
    }
}

// Function to peek at the front element of the queue
void peek(int* queue, int front) {
    if (front == -1) {
        printf("Queue is empty. No elements to peek.\n");
    } else {
        printf("Front element is: %d\n", queue[front]);
    }
}

// Main function
int main() {
    int queue[MAXSIZE];
    int front = -1, rear = -1;
    int choice, value;
    
    while (1) {
        printf("\nQueue Operations:\n");
        printf("1. Enqueue\n");
        printf("2. Dequeue\n");
        printf("3. Display\n");
        printf("4. Peek\n");
        printf("5. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);
        
        switch (choice) {
            case 1:
                printf("Enter the value to enqueue: ");
                scanf("%d", &value);
                enqueue(queue, &front, &rear, value);
                break;
            case 2:
                dequeue(queue, &front, &rear);
                break;
            case 3:
                display(queue, front, rear);
                break;
            case 4:
                peek(queue, front);
                break;
            case 5:
                printf("Exiting...\n");
                return 0;
            default:
                printf("Invalid choice! Please try again.\n");
        }
    }
}
