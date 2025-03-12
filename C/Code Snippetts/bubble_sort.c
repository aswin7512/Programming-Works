//program to implement bubble sort
#include<stdio.h>


void swap(int *a, int *b){
    int temp;
    temp = *a;
    *a = *b;
    *b = temp;
}


void read_arr(int a[], int n){
    printf("ENTER ELEMENTS OF THE ARRAY\n");
    for(int i = 0; i < n; i++){
        printf("ENTER ELEMENT %d: ", i+1);
        scanf("%d", &a[i]);
    }
}


void disp_arr(int a[], int n){
    printf("ARRAY: ");
    for(int i = 0; i < n; i++){
        printf("%d, ", a[i]);
    }
}


void bubble_sort(int a[], int n){
    for(int i = 0; i < n; i++){
        for(int j = 0; j < n-1-i; j++){
            if(a[j] > a[j+1])
                swap(&a[j], &a[j+1]);
        }
    }
}


int main(){
    int a[25], n;
    printf("ENTER NO. OF ELEMENTS: ");
    scanf("%d", &n);
    read_arr(a, n);
    printf("IMPLEMENTING BUBBLE SORT...\n");
    bubble_sort(a, n);
    printf("SUCCESSFULLY SORTED...\n");
    disp_arr(a, n);
    return 0;
}