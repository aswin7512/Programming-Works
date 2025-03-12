#include<stdio.h>
int main(){
    int sp[][3] = {
            {3, 4, 6}, 
            {0, 2, 3}, 
            {0, 3, 5}, 
            {1, 0, 4}, 
            {1, 2, 9},
            {2, 1, 5},
            {2, 3, 2}
            }, spt[7][3], k = 0;
    spt[0][0] = sp[0][1];
    spt[0][1] = sp[0][0];
    spt[0][2] = sp[0][2];
    for(int i = 0; i < sp[0][1]; i++){
        for(int j = 0; j <= sp[0][2]; j++){
            if(sp[j][1] == i){
                spt[++k][0] = sp[j][1];
                spt[k][1] = sp[j][0];
                spt[k][2] = sp[j][2];
            }
        }
    }

    for(int i = 0; i <= spt[0][2]; i++){
        for(int j = 0; j < 3; j++){
            printf("%3d", spt[i][j]);
        }
        printf("\n");
    }
}