//program to implement bubble sort
#include<stdio.h>
int main(){
    int a[10],s,t;
    printf("ENTER THE NO. OF ELEMENTS TO STORE: ");
    scanf("%d",&s);
    for(int i=0;i<s;i++){
        printf("ENTER ELEMENT %d: ",i+1);
        scanf("%d",&a[i]);
    }
    for(int i=0;i<s;i++){
        for(int j=0;j<s;j++){
            if(a[j]>a[j+1]){
                t=a[j];
                a[j]=a[j+1];
                a[j+1]=t;
            }
        }
    }
    printf("SORTED ARRAY IS\n");
    for(int i=0;i<s;i++){
        printf("%d ",a[i]);
    }
    return 0;
}