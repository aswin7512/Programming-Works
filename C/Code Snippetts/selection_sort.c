//program to implement selection sort
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


int find_min(int a[], int n, int i){
    int pos = i;
    for(int j = i+1; j < n; j++){
        if (a[pos] > a[j]){
            pos = j;
        }
    }
    return pos;
}


void disp_arr(int a[], int n){
    printf("ARRAY: ");
    for(int i = 0; i < n; i++){
        printf("%d, ", a[i]);
    }
}


void selection_sort(int a[], int n){
    int pos;
    for(int i = 0; i < n; i++){
        pos = find_min(a, n, i);
        swap(&a[i], &a[pos]);
    }
}


int main(){
    int a[25], n;
    printf("ENTER NO. OF ELEMENTS: ");
    scanf("%d", &n);
    read_arr(a, n);
    printf("IMPLEMENTING SELECTION SORT...\n");
    selection_sort(a, n);
    printf("SUCCESSFULLY SORTED...\n");
    disp_arr(a, n);
    return 0;
}