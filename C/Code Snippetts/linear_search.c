//program to implement linear search
#include<stdio.h>

void read_array(int a[], int n){
    printf("ENTER ELEMENTS OF THE ARRAY\n");
    for(int i = 0; i < n; i++){
        printf("ELEMENT %d: ", i+1);
        scanf("%d", &a[i]);
    }
}


int linear_search(int a[], int key, int n){
    int found = 0;
    for(int i = 0; i < n; i++){
        if (a[i] == key){
            found = i + 1;
            break;
        }
    }
    return found;
}


int main(){
    int arr[20], n, key, found;
    printf("ENTER NO. OF ELEMENTS: ");
    scanf("%d",&n);
    read_array(arr, n);
    printf("ENTER KEY TO SEARCH IN ARRAY: ");
    scanf("%d",&key);
    found = linear_search(arr, key, n);
    if (found)
        printf("%d FOUND AT POSITION %d", key, found);
    else
        printf("%d NOT FOUND", key);
    return 0;
}