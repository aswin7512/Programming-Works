#include<stdio.h>
int main(){
    int a[20],n,s,p=0;
    printf("ENTER THE NO. OF ELEMENTS: ");
    scanf("%d",&n);
    for(int i=0;i<n;i++){
        printf("ENTER ELEMENT %d: ",i+1);
        scanf("%d",&a[i]);
    }
    printf("ENTER NUMBER TO SEARCH: ");
    scanf("%d",&s);
    for(int i=0;i<n;i++){
        if(a[i]==s){
            p=i+1;
            break;
        }
    }
    p!=0?printf("%d FOUND AT POSITION %d",s,p):printf("%d NOT FOUND",s);
    return 0;
}