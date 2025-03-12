#include<stdio.h>

void merge(int a[], int l, int m, int u) {
    int i = l, j = m+1, k = 0, temp[u - l];
    while (i <= m && j <= u) {
        if (a[i] <= a[j])
            temp[k++] = a[i++];
        else
            temp[k++] = a[j++];
    }
    while (i <= m)
        temp[k++] = a[i++];
    while (j <= u)
        temp[k++] = a[j++];
    for (int i = l, k = 0; i <= u; i++, k++)
        a[i] = temp[k];
}

void mergesort(int a[], int l, int u) {
    if (l < u) {
        int m = (l + u)/ 2;
        mergesort(a, l, m);
        mergesort(a, m+1, u);
        merge(a, l, m, u);
    }
}

int main() {
    int a[] = {1, 9, 5, 7, 2, 10, 4, 6, 3, 8};
    int l = 0, u = 10;
    mergesort(a, l, u);
    for (int i = 0; i < 10; i++) 
        printf("%d, ", a[i]);
    return 0;
}