#include<stdio.h>
int main(){
    int a[20],n,s=0;
    printf("ENTER THE NO. OF ELEMENTS: ");
    scanf("%d",&n);
    for(int i=0;i<n;i++){
        printf("ENTER ELEMENT %d: ",i+1);
        scanf("%d",&a[i]);
        s+=a[i];
    }
    printf("SUM OF ELEMENTS OF THE GIVEN ARRAY = %d",s);
    return 0;
}