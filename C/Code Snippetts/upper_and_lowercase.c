//program to count the no. of uppercase and lower case letters
#include<stdio.h>
int main(){
    char a[20];
    int u=0,l=0;
    printf("ENTER A STRING: ");
    scanf("%s",&a);
    for(int i=0;a[i]!='\0';i++){
        if(a[i]>='A' && a[i]<='Z'){
            u+=1;
        }
        else if(a[i]>='a' && a[i]<='z'){
            l+=1;
        }
    }
    printf("No. of upper case characters: %d\nNo. of lower case characters: %d",u,l);
    return 0;
}