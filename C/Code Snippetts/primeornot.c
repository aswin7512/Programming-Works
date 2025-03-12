//TO CHECK WHETHER A NUMBER IS PRIME OR NOT
#include<stdio.h>
int main(){
    int a,p=0;
    printf("ENTER A NUMBER: ");
    scanf("%d",&a);
    for(int i=2;i<a;i++){
      if(a%i==0){
        p=1;
      }
    }
    if(p==0){
        printf("GIVEN NUMBER IS PRIME");
    }
    else{
        printf("GIVEN NUMBER IS COMPOSITE");
    }
}