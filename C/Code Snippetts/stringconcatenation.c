//program to perform string concatenation
#include<stdio.h>
int main(){
    char a[20],b[20],c[40];
    int ct=0;
    printf("ENTER TWO STRINGS: ");
    scanf("%s %s",&a,&b);
    for(int i=0;a[i]!='\0';i++){
        c[ct]=a[i];
        ct++;
    }
    for(int i=0;b[i]!='\0';i++){
        c[ct]=b[i];
        ct++;
    }
    c[ct]='\0';
    printf("CONCATENATED STRING IS: %s",c);
    return 0;
}