//program to implement insertion sort
#include<stdio.h>


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


void insertion_sort(int a[], int n){
    int j, pivot;
    for(int i = 0; i < n; i++){
        pivot = a[i];
        for(j = i-1; j >= 0; j--){
            if(a[j] > pivot){
                a[j+1] = a[j];
            }
            else
                break;
        }
        a[j+1] = pivot;
    }
}


int main(){
    int a[25], n;
    printf("ENTER NO. OF ELEMENTS: ");
    scanf("%d", &n);
    read_arr(a, n);
    printf("IMPLEMENTING INSERTION SORT...\n");
    insertion_sort(a, n);
    printf("SUCCESSFULLY SORTED...\n");
    disp_arr(a, n);
    return 0;
}