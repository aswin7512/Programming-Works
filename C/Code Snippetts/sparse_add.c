//program to implement sparse addition
#include<stdio.h>


void read_mat(int sp[][3], int m, int n){
    int e, k=0;
    for(int i = 0; i < m; i++)
        for(int j = 0; j < n; j++){
            printf("ENTER ELEMENT A%d%d: ", i+1, j+1);
            scanf("%d", &e);
            if(e != 0){
                sp[++k][0] = i;
                sp[k][1] = j;
                sp[k][2] = e;
            }
        }
    sp[0][0] = m;
    sp[0][1] = n;
    sp[0][2] = k;
}


void print_mat(int sp[][3]){
    for(int i = 0; i <= sp[0][2]; i++){
        for(int j = 0; j < 3; j++)
            printf("%3d", sp[i][j]);
        printf("\n");
    }
}


void add_sparse(int sp1[][3], int sp2[][3], int spr[][3]){
    int i = 1, j = 1, k = 0, sum;
    while(i <= sp1[0][2] && j <= sp2[0][2]){
        if(sp1[i][0] == sp2[j][0]){
            if(sp1[i][1] == sp2[j][1]){
                sum = sp1[i][2] + sp2[j][2];
                if(sum != 0){
                    spr[++k][0] = sp1[i][0];
                    spr[k][1] = sp1[i][1];
                    spr[k][2] = sum;
                }
                i++;
                j++;
            }
            else if(sp1[i][1] < sp2[j][1]){
                spr[++k][0] = sp1[i][0];
                spr[k][1] = sp1[i][1];
                spr[k][2] = sp1[i++][2];
            }
            else{
                spr[++k][0] = sp2[j][0];
                spr[k][1] = sp2[j][1];
                spr[k][2] = sp2[j++][2];
            }
        }
        else if(sp1[i][0] < sp2[j][0]){
            spr[++k][0] = sp1[i][0];
            spr[k][1] = sp1[i][1];
            spr[k][2] = sp1[i++][2];
        }
        else{
            spr[++k][0] = sp2[j][0];
            spr[k][1] = sp2[j][1];
            spr[k][2] = sp2[j++][2];
        } 
    }
    while(i <= sp1[0][2]){
        spr[++k][0] = sp1[i][0];
        spr[k][1] = sp1[i][1];
        spr[k][2] = sp1[i++][2];
    }
    while(j <= sp2[0][2]){
        spr[++k][0] = sp2[j][0];
        spr[k][1] = sp2[j][1];
        spr[k][2] = sp2[j++][2];
    }
    spr[0][0] = sp1[0][0];
    spr[0][1] = sp1[0][1];
    spr[0][2] = k;
}


int main(){
    int sp1[20][3], sp2[20][3], spr[20][3], m, n;
    printf("ENTER NO. OF ROWS AND COLUMNS: ");
    scanf("%d %d", &m, &n);
    printf("ENTER MATRIX 1\n");
    read_mat(sp1, m, n);
    printf("ENTER MATRIX 2\n");
    read_mat(sp2, m, n);
    printf("ADDING MATRICES...\n");
    add_sparse(sp1, sp2, spr);
    printf("ADDITION SUCCESSFULL...\n");
    printf("RESULTANT SPARSE REPRESENTATION...\n");
    print_mat(spr);
    return 0;
}