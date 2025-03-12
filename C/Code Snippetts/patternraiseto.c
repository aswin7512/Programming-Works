#include<stdio.h>
int main(){
    int a,c;
    printf("ENTER A NUMBER: ");
    scanf("%d",&a);
    for(int i=a;i>0;i--){
        for(int j=1;j<=i;j++){
            c=1;
            for(int k=1;k<=i;k++){
                c*=j;
            }
            printf("%d ",c);
        }
        printf("\n");
    }
    return 0;
}