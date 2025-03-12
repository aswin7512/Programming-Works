//program to implement binary search
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


int binary_search(int a[], int n, int key){
    int start = 0, end = n - 1, mid;
    mid = (start + end)/2;
    while(start <= end){
        if (a[mid] == key){
            return mid + 1;
        }
        else if(a[mid] > key){
            end = mid - 1;
        }
        else{
            start = mid + 1;
        }
        mid = (start + end)/2;
    }
    return 0;
}


int main(){
    int a[25], n, key, found;
    printf("ENTER NO. OF ELEMENTS: ");
    scanf("%d", &n);
    read_arr(a, n);
    disp_arr(a, n);
    printf("\nENTER KEY TO SEARCH: ");
    scanf("%d", &key);
    printf("SEARCHING FOR %d...\n", key);
    found = binary_search(a, n, key);
    if(found)
        printf("%d FOUND AT POSITION %d", key, found);
    else
        printf("%d NOT FOUND", key);
    return 0;
}